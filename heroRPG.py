#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self):
        self.health = 10
        self.power = 5
    
    def attack(self, goblin):
        goblin.health -= self.power
        print(f"You do {self.power} damage to the goblin.")
        
        if goblin.health <= 0:
            print("The goblin is dead.")
        


class Goblin:
    def __init__(self):
        self.health = 6
        self.power = 2
        
    def attack(self, hero):
        hero.health -= goblin.power
        print(f"The goblin does {goblin.power} damage to you.")
            
        if hero.health <= 0:
            print("You are dead.")

def main():

    hero = Hero()
    goblin = Goblin()

    while (goblin.health) > 0 and (hero.health > 0):
        
        print(f"You have {hero.health} health and {hero.power} power.")
        print(f"The goblin has {goblin.health} health and {goblin.power} power.")
        
        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
        raw_input = input()
        
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print(f"Invalid input {raw_input}")

        if goblin_health > 0:
            # Goblin attacks hero
            goblin.attack(hero)


main()
