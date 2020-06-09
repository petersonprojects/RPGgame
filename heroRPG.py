#!/usr/bin/env python
import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, character, other_char, random):

        if(random == True):
            dmgAfterArmor = int((self.power - character.armor_rating)*2)
            
            if character.armor_rating >= self.power:
                dmgAfterArmor = 0
            
            character.health = character.health - dmgAfterArmor
            print(f"The {other_char} does {dmgAfterArmor} damage to the {character.name}.")

            random = False
        
        else:
            dmgAfterArmor = self.power - character.armor_rating
            
            if character.armor_rating >= self.power:
                dmgAfterArmor = 0
            
            character.health = character.health - dmgAfterArmor
            print(f"The {other_char} does {dmgAfterArmor} damage to the {character.name}.")
    
    def alive(self):
        if self.health > 0:
            alive = True
        elif self.health <= 0:
            alive = False
        
        return alive
    
    def print_status(self, character):
        print(f"The {character} has {self.health} health, {self.power} power, and {self.armor_rating} armor rating.")

class Hero(Character):
    def __init__(self):
        self.name = "hero"
        self.health = 50
        self.power = 5
        self.coins = 10
        self.armor_rating = 0
        self.evasion = 0
    
    def attack(self, character, other_char):
        if(random.randint(1,10) <= 2):
            isDblDmg = True
        else:
            isDblDmg = False
        
        super(Hero,self).attack(character, other_char, isDblDmg)
    
    def buy(self, hero, item):
        if(self.coins >= item.cost):
            self.coins -= item.cost
            item.apply(hero)
        else:
            print("You don't have enough coins to buy this item.")
            
        
class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "goblin"
        self.bounty = 5
        self.armor_rating = 0
        self.evasion = 0
        
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
        self.health = 30
        self.power = 3
        self.name = "medic"
        self.bounty = 10
        self.armor_rating = 0
        self.evasion = 0
        
    def restore(self):
        self.health = self.health+2

class Shadow(Character):
    def __init__(self):
        self.health = 5
        self.power = 3
        self.name = "shadow"
        self.bounty = 10
        self.armor_rating = 0
        self.evasion = 0
        
        
class Behemoth(Character):
    def __init__(self):
        self.health = 150
        self.power = 6
        self.name = "behemoth"
        self.bounty = 100
        self.armor_rating = 4
        self.evasion = 0
        

class Bard(Character):
    def __init__(self):
        self.health = 55
        self.power = 4
        self.name = "bard"
        self.bounty = 35
        self.armor_rating = 0
        self.evasion = 0
        
        
class Battle():
    
    def do_battle(self, hero, enemy):
        
        print("========================")
        print(f"Hero faces the {enemy.name}.")
        print("========================")
        
        
        while enemy.alive() and hero.alive():
            
            hero.print_status("hero")
            enemy.print_status(enemy.name)
            
            print("========================")
            print("\nWhat do you want to do?")
            print(f"1. fight the {enemy.name}")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')

            raw_input = input()
            
            print("")
            
            if raw_input == "1":
                
                if(enemy.name == 'bard'):
                    bardchance = random.randint(1,10)
                    
                    if(bardchance >= 7):
                        print("\nThe bard charmed you into attacking yourself!\n")
                        hero.attack(hero, "hero")
                    elif bardchance < 7:
                        hero.attack(enemy, "hero")
                
                elif(enemy.name == "medic"):
                    medicchance = random.randint(1,10)
                    if(medicchance <= 2):
                        enemy.restore()
                        print("Medic restored 2 health points.")
                    hero.attack(enemy, "hero")
                
                elif(enemy.name == "shadow"):
                    shadowchance = random.randint(1,10)
                    
                    if(shadowchance != 4):
                        print("\nShadow dodged the attack.\n")
                    
                    elif(shadowchance == 4):
                        hero.attack(enemy, "hero")
                else:
                    hero.attack(enemy, "hero")
                
            elif raw_input == "2":
                if (enemy.name == "medic"):
                    medicchance = random.randint(1,10)
                    if(medicchance <= 2):
                        enemy.restore()
                        print("Medic restored 2 health points while you did nothing.")

            elif raw_input == "3":
                print("\nGoodbye.\n")
                break
            else:
                print(f"Invalid input {raw_input}")

            if enemy.health > 0:
                enemy.attack(hero, enemy.name, False)
                
            elif enemy.name == 'zombie':
                enemy.attack(hero, enemy.name, False)
                
        if hero.alive():
            print(f"You've defeated the {enemy.name} and gained {enemy.bounty} coins.")
            hero.coins += enemy.bounty
            return True
        else:
            return False
        
class Tonic():
    cost = 5
    name = "tonic"
    def apply(self, hero):
        hero.health += 10
        print(f"\nHero's health increased to {hero.health}\n")

class Sword():
    cost = 10
    name = "sword"
    def apply(self, hero):
        hero.power += 2
        print(f"\nHero's power increased to {hero.power}.\n")
        
class SuperTonic():
    cost = 20
    name = "super tonic"
    def apply(self, hero):
        hero.health += 50
        print(f"\nHero's health inscread to {hero.health}.\n")

class Armor():
    cost = 15
    name = "armor"  
    def apply(self, hero):
        hero.armor_rating += 2 
        print(f"\nHero now has armor rating of {hero.armor_rating}.\n")

class Evade():
    cost = 25
    name = "evade"
    def apply(self, hero):
        hero.evasion += 2
        print(f"\nHero now has evasion rating of {hero.evasion}.\n")
        
class Shop():
    items = [Tonic, Sword, SuperTonic, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print("====================")
            print("Welcome to The Shop!")
            print("====================")
            print(f"You have {hero.coins} coins.")
            print("What do you want to do?")
            for i in range(len(Shop.items)):
                item = Shop.items[i]
                print(f"{i+1}. buy {item.name} ({item.cost})")
            print("10. leave shop")
            
            answer = input("> ")
            intAnswer = int(answer)
            
            if answer == '':
                print("Invalid input.")
            elif intAnswer == 10:
                break
            else:
                itemToBuy = Shop.items[intAnswer-1]
                item = itemToBuy()
                hero.buy(hero, item)
def main():

    hero = Hero()
    battle_engine = Battle()
    shopping_engine = Shop()
    enemies = [Goblin(),Shadow(),Medic(),Bard(),Behemoth()]

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero,enemy)
        if not hero_won:
            print("Your hero died.")
            break
        
        if(enemy.name == "behemoth" and enemy.alive() == False):
            print("*******************************")
            print("Congratulations! You've won!")
            print("*******************************")
            break
        
        shopping_engine.do_shopping(hero)
        


main()
