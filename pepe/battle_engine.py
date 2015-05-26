#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
pepe.battle_engine.py
AUTHOR: on_three
DATE: Monday May 25th 2015
DESC: Simple image combat in the spirit of old UPC battles
'''

import argparse

from random import randint

class Pepe(object):
  def __init__(self, image_url):
    self._image_url = image_url
    self._attack = 0
    self._defense = 0
    self._hit_points = 0
    self.init()

  def init(self):
    '''
    Initialize own attack, defense etc via image qualities
    '''
    self._attack = randint(1,50)
    self._defense = randint(1,50)
    self._hit_points = randint(10,50)

  @property
  def hit_points(self):
    return self._hit_points

  def damage(self, d):
    self._hit_points -= d
    if self._hit_points<0:
      self._hit_points = 0

  @property
  def attack(self):
    return self._attack

  @property
  def defense(self):
    return self._defense

  def __unicode__(self):
    return u'Attack: {attack} Defense: {defense} Hit Points: {hit_points} '.format( \
      attack=unicode(self.attack),\
      defense=unicode(self.defense),\
      hit_points=unicode(self.hit_points))

class Combat(object):
  def __init__(self, pepe_1, pepe_2):
    self._p1 = pepe_1
    self._p2 = pepe_2
    self._combat = []
    self.do_combat()

  def do_combat(self):
    #self._combat.append(u'pepe 1 wins')

    #pepe 1 will always go first for now
    #TODO: decide randomly who goes first via attack
    attacker = self._p1
    defender = self._p2
    while self._p1.hit_points>0 and self._p2.hit_points>0:
      #chance of hit is 50 + (attacker.attack - defender.defense)
      #so if both 50, we get 50% chance of hit
      #if attacker 50, and defender 1 we get 99% chance of hit
      #if attacker 1 and defender 50 we get 1% chance of hit
      hit_chance = 50 + (attacker.attack - defender.defense)
      roll = randint(1,100)
      hit = roll < hit_chance
      #randomly figure damage in a similar manner to hit chance
      damage_percent = (int)((float) (randint(1,100)*(attacker.attack - defender.defense)))
      #print str(damage_percent)
      damage = randint(1,100) + (int)(damage_percent/100.0)
      if hit and damage > 0:
        self._combat.append(u'Hit for {damage} points'.format(damage=unicode(damage)))
        defender.damage(damage)
      else:
        self._combat.append(u'Miss')

      #swam attacker and defender for next round
      tmp = defender
      defender = attacker
      attacker = tmp
    if self._p1.hit_points > 0:
      self._combat.append(u'Pepe 1 wins')
    else:
      self._combat.append(u'Pepe 2 wins')

  def __unicode__(self):
    result = u''
    for i,r in enumerate(self._combat):
      result += r + u'\n'
    return result


def main():
  parser = argparse.ArgumentParser(description='Pepe fight test.')
  parser.add_argument('pepe_1', help='Url to first pepe input image.', type=str)
  parser.add_argument('pepe_2', help='Url to second pepe input image.', type=str)
  #parser.add_argument('-u', '--username', help='Username this server uses at IRC server signon.', type=str, default='')
  args = parser.parse_args()

  pepe_1 = Pepe(args.pepe_1)
  print 'pepe 1: ' + unicode(pepe_1).format('utf-8')
  pepe_2 = Pepe(args.pepe_2)
  print 'pepe 2: ' + unicode(pepe_2).format('utf-8')

  #let the two fight it out
  results = Combat(pepe_1, pepe_2)
  print unicode(results).encode('utf-8')

if __name__ == "__main__":
  main()
