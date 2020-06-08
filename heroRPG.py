#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self):
        self.health = 10
        self.power = 5
    
    def attack(self, goblin_health)
        goblin_health -= self.power
        print(f"You do {self.power} damage to the goblin.")
        
        if goblin_health <= 0:
            print("The goblin is dead.")

    
class Goblin:
    def __init__(self):
        self.health = 6
        self.power = 2
        

def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2

    while goblin_health > 0 and hero_health > 0:
        print(f"You have {hero_health} health and {hero_power} power.")
        print(f"The goblin has {goblin_health} health and {goblin_power} power.")
        
        print("\nWhat do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        
        raw_input = input()
        
        if raw_input == "1":
            # Hero attacks goblin
            # .attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")


main()
