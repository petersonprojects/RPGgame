#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, character, other_char):
        character.health -= self.power
        print(f"The {other_char} does {self.power} damage to the {character.name}.")
        
        if character.health <= 0:
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

class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "goblin"

def main():

    hero = Hero()
    goblin = Goblin()

    while goblin.alive() and hero.alive():
        
        hero.print_status("hero")
        goblin.print_status("goblin")
        
        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
        raw_input = input()
        
        if raw_input == "1":
            hero.attack(goblin, "hero")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin.health > 0:
            goblin.attack(hero, "goblin")


main()
