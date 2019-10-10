#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 23:58:55 2019

@author: dominicong
"""


class Poke:
    
    def __init__(self,pokemon_type):
        self.pokemon_type = pokemon_type
        self.health = 100
        self.attack = 10
        self.special_attack = 7
        self.special_defense = 5
        self.defense = 5
        
    def pound(self,enemy):
        enemy.health -= (self.attack-enemy.defense)
        
    def ember(self,enemy):
        enemy.health -= (self.special_attack*1.5-enemy.special_defense)
        
    def growl(self,enemy):
        enemy.defense -= 5
    
    def scratch(self,enemy):
        enemy.health -= (self.attack-enemy.defense)
        
    def bubble(self,enemy):
        if (self.pokemon_type == 'water' and enemy.pokemon_type == 'fire'):
            enemy.health -= (self.special_attack*2-enemy.special_defense/2)
        else:
            enemy.health -= (self.special_attack-enemy.special_defense)

    
    def get_health(self):
        return self.health
    
    
    
    
    
    
    
    