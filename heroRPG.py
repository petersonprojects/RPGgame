#!/usr/bin/env python
import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, character, other_char, random):

        if(random == True):
            self.power = self.power*2
            character.health -= self.power
            print(f"The {other_char} does {self.power} damage to the {character.name}.")
            self.power = int((self.power)/2)
            random = False
        
        else:
            character.health -= self.power
            print(f"The {other_char} does {self.power} damage to the {character.name}.")
        
        if(character.name != 'zombie') and character.health <= 0:
            print(f"The {character.name} is dead.")
    
    def alive(self):
        if self.health > 0:
            alive = True
        elif self.health <= 0:
            alive = False
        
        return alive
    
    def print_status(self, character):
        print(f"The {character} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self):
        self.health = 10
        self.power = 5
        self.name = "hero"
    
    def attack(self, character, other_char):
        if(random.randint(1,10) <= 2):
            isDblDmg = True
        else:
            isDblDmg = False
        
        super(Hero,self).attack(character, other_char, isDblDmg)
        

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "goblin"

class Zombie(Character):
    def __init__(self):
        self.health = 0
        self.power = 1
        self.name = "zombie"

    def alive(self):
        return True
    
    def print_status(self, character):
        print(f"The zombie has 0 health and 1 power.")
    
class Medic(Character):
    def __init__(self):
        self.health = 20
        self.power = 3
        self.name = "medic"
        
    def restore(self):
        self.health = self.health+2

class Shadow(Character):
    def __init__(self):
        self.health = 1
        self.power = 5
        self.name = "shadow"
        
def main():

    hero = Hero()
    #goblin = Goblin()
    enemy = Zombie()

    while enemy.alive() and hero.alive():
        
        hero.print_status("hero")
        enemy.print_status(f"{enemy.name}")
        
        print("\nWhat do you want to do?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
        raw_input = input()
        
        if raw_input == "1":
            if(enemy.name == "medic" and random.randint(1,10) <= 2):
                enemy.restore()
                print("Medic restored 2 health points.")
                
            hero.attack(enemy, "hero")  
            
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("\nGoodbye.\n")
            break
        else:
            print(f"Invalid input {raw_input}")

        if enemy.health > 0:
            enemy.attack(hero, enemy.name, False)
        elif enemy.name == 'zombie':
            enemy.attack(hero, enemy.name, False)

main()
