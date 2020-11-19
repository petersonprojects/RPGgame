#!/usr/bin/env python
import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.armor_rating = 0
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0
    
    def attack(self, character, dblDmg, enemy):
        evasion = random.random()
        
        if(character.evasion >= .99):
            character.evasion = .99
        
        if(dblDmg == True):
            
            if(character.evasion >= evasion or character.fullevasion > 0):
                print(f"\n\v\t{character.name} evaded the attack from {enemy.name}!\n")
                character.fullevasion -= 1
            
            else:
                dmgAfterArmor = int((self.power - character.armor_rating)*2)
                
                if character.armor_rating >= self.power:
                    dmgAfterArmor = 0
                
                character.health = character.health - dmgAfterArmor
                print(f"\t\t\tThe {enemy.name} does {dmgAfterArmor} damage to the {character.name}.\n")
                
            if self.swapCounter > 0:
                self.swapCounter = self.swapCounter - 1
                Swap.expire(self,character,enemy)
            dblDmg = False
        
        else:
            if(character.evasion >= evasion or character.fullevasion > 0):
                print(f"\n\v\t{character.name} evaded the attack from {enemy.name}!\n")
                character.fullevasion -= 1
            else:
                dmgAfterArmor = self.power - character.armor_rating
                
                if character.armor_rating >= self.power:
                    dmgAfterArmor = 0
                
                character.health = character.health - dmgAfterArmor
                print(f"\v\t\t\tThe {enemy.name} does {dmgAfterArmor} damage to the {character.name}.\n")
                
            if self.swapCounter > 0:
                self.swapCounter = self.swapCounter - 1
                Swap.expire(self, character, enemy)
    
    def alive(self):
        if self.health > 0:
            alive = True
        elif self.health <= 0:
            alive = False
        
        return alive
    
    def print_status(self, character):
        evasion = int(self.evasion*100)
        print(f"\tThe {character} has {self.health} health, {self.power} power, {self.armor_rating} armor rating, and {evasion}% evasion.")

class Hero(Character):
    def __init__(self):
        self.max = 50
        self.maxArmor = 6
        self.name = "hero"
        self.health = 50
        self.power = 5
        self.coins = 10
        self.inventory = []
        self.armor_rating = 0
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0
    
    def attack(self, character, enemy):
        if(random.randint(1,10) <= 2):
            isDblDmg = True
        else:
            isDblDmg = False
        
        super(Hero,self).attack(character, isDblDmg, enemy)
    
    def buy(self, hero, item):
        if(self.coins >= item.cost):
            self.coins -= item.cost

        else:
            print("\t\tYou don't have enough coins to buy this item.")
        
class Goblin(Character):
    def __init__(self):
        self.health = 6
        self.power = 2
        self.name = "goblin"
        self.bounty = 5
        self.armor_rating = 0
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0
        
class Zombie(Character):
    def __init__(self):
        self.health = 0
        self.power = 4
        self.name = "zombie"
        self.bounty = 5
        self.armor_rating = 0
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0
        
    def alive(self):
        return True
    
    def print_status(self, character):
        print(f"\t\tThe zombie has 0 health and {self.power} power.")
    
class Medic(Character):
    def __init__(self):
        self.health = 30
        self.power = 3
        self.name = "medic"
        self.bounty = 15
        self.armor_rating = 0
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0

    def restore(self):
        self.health = self.health+10

class Shadow(Character):
    def __init__(self):
        self.health = 5
        self.power = 1
        self.name = "shadow"
        self.bounty = 15
        self.evasion = 0.9
        self.armor_rating = 0
        self.fullevasion = 0
        self.swapCounter = 0
        
class Behemoth(Character):
    def __init__(self):
        self.health = 150
        self.power = 7
        self.name = "behemoth"
        self.bounty = 1000
        self.armor_rating = 3
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0
        
class Bard(Character):
    def __init__(self):
        self.health = 40
        self.power = 4
        self.name = "bard"
        self.bounty = 35
        self.armor_rating = 1
        self.evasion = 0
        self.fullevasion = 0
        self.swapCounter = 0
        
class Battle():
    def do_battle(self, hero, enemy):
        
        print(f""" \n\n
         _         | |
        | | _______| |---------------------------------------------\\
        |:-)_______|==[]============================================>
        |_|        | |---------------------------------------------/
                   |_|

                        =============================
                        A wild {enemy.name} appears!
                        =============================
            """)
        
        if(enemy.name == "goblin"):
            print("""
                          .-\"\"\"\".
                         /       \\
                     __ /   .-.  .\\
                    /  `\  /   \/  \\
                    |  _ \/   .==.==.
                    | (   \  /____\__\\
                    \ \      (_()(_()
                     \ \            '---._
                      \                   \_
                   /\ |`       (__)________/
                  /  \|     /\___/
                 |    \     \||VV
                 |     \     \|\"\"\"\"\,
                 |      \     ______|
                  \       \  /`
                           \(
            """)
        elif(enemy.name == "zombie"):
            print("""
                        _,--~~~,
                       .'        `.
                       |           ;
                       |           :
                      /_,-==/     .'
                    /'`\*  ;      :      
                  :'    `-        :      
                  `~*,'     .     :      
                     :__.,._  `;  :      
                     `\'    )  '  `,     
                         \-/  '     )     
                         :'          \ _
                          `~---,-~    `,)
          ___                   \     /~`\\
    \---__ `;~~~-------------~~~(| _-'    `,
  ---, ' \`-._____     _______.---'         \\
 \--- `~~-`,      ~~~~~~                     `,
\----      )                                   \\
\----.  __ /                                    `-
 \----'` -~____  
               ~~~~~--------,.___     
                                 ```\_
                  """)
        
        
        while enemy.alive() and hero.alive():
            
            hero.print_status("hero")
            enemy.print_status(enemy.name)
            
            print(f"""
                
                        ========================
                        
                        What do you want to do?
                        
                        1. fight the {enemy.name}
                        2. do nothing
                        3. flee
                        4. open inventory
                        
                        ========================
                
                """)
            print("> ", end=' ')

            try:
                inputError = False
                selection = int(input())
            except ValueError:
                print("\nInvalid input. Try again.")
                inputError = True
                
            print("")
            
            if selection == 1:
                if(enemy.name == 'bard'):
                    bardchance = random.randint(1,10)
                    
                    if(bardchance >= 8):
                        print("\nThe bard charmed you into attacking yourself!\n")
                        hero.attack(hero,enemy)
                    elif bardchance < 8:
                        hero.attack(enemy,hero)
                
                elif(enemy.name == "medic"):
                    medicchance = random.randint(1,10)
                    if(medicchance <= 2):
                        enemy.restore()
                        print("Medic restored 2 health points.")
                    hero.attack(enemy,hero)
                
                else:
                    hero.attack(enemy,hero)
                
            elif selection == 2:
                if (enemy.name == "medic"):
                    medicchance = random.randint(1,10)
                    if(medicchance <= 2):
                        enemy.restore()
                        print("Medic restored 2 health points while you did nothing.")

            elif selection == 3:
                print(f"\nHero fled from {enemy.name}.\n")
                break
            
            elif selection == 4:
                while True:
                    print("""
                                ,-.
                               ("O_)
                              / `-/
                             /-. /
                            /   )
                           /   /  
              _           /-. /
             (_)"-._     /   )
               "-._ "-'""( )/        ====================
                   "-/"-._" `.       |     Inventory    |
                    /     "-.'._     ====================
                   /\       /-._"-._
    _,---...__    /  ) _,-"/    "-(_)
___<__(|) _   ""-/  / /   /
 '  `----' ""-.   \/ /   /
               )  ] /   /
       ____..-'   //   /                       )
   ,-""      __.,'/   /   ___                 /,
  /    ,--""/  / /   /,-""   \"\"\"-.          ,'/
 [    (    /  / /   /  ,.---,_   `._   _,-','
  \    `-./  / /   /  /       `-._  \"\"\" ,-'
   `-._  /  / /   /_,'            ""--"
       "/  / /   /"         
       /  / /   /
      /  / /   /  
     /  |,'   /  
    :   /    /
    [  /   ,'   
    | /  ,'
    |/,-'
    P'
                            
                    """)
                    for i in range(len(hero.inventory)):
                        print(f"\t\t\t{i+1}. Use {hero.inventory[i].name}")
                    print(f"\t\t\t{len(hero.inventory)+1}. Exit")
                    
                    try:
                        iteminput = int(input("> "))
                        
                    except ValueError:
                        print("\n\t\t\tInvalid input. Try again. Value Error")

                    if iteminput == len(hero.inventory)+1:
                        break
                    elif iteminput > 0 and iteminput <= len(hero.inventory):
                        if(hero.inventory[iteminput-1].name == 'swap'):
                            hero.inventory[iteminput-1].apply(hero, enemy)
                        else:
                            hero.inventory[iteminput-1].apply(hero)

                        del hero.inventory[iteminput-1]
                        
            elif selection > 4:
                print("\nInvalid input. Try again.")
                inputError = True
                
            if enemy.health > 0 and inputError == False:
                enemy.attack(hero, False, enemy)
                            
            elif enemy.name == 'zombie':
                enemy.attack(hero, False, enemy)
            
        if hero.alive():
            if not(enemy.alive()):
                print("""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~\%\%',
  (                     %  Y
 {                      \%\% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
                                """)
                print(f"\n\t\t\tYou've defeated the {enemy.name} and gained {enemy.bounty} coins.")
                
                hero.coins += enemy.bounty
            return True
        else:
            return False
        
## items and shop
        
class Tonic():
    cost = 5
    name = "tonic"
    def apply(self, hero):
        hero.health += 10
        if hero.health > hero.max:
            hero.health = hero.max
        print(f"\n\t\t\tHero's health increased to {hero.health}\n")

class Sword():
    cost = 10
    name = "sword"
    def apply(self, hero):
        hero.power += 2
        print(f"\n\t\t\tHero's power increased to {hero.power}.\n")
        
class SuperTonic():
    cost = 20
    name = "super tonic"
    def apply(self, hero):
        hero.health += 50
        if hero.health > hero.max:
            hero.health = hero.max
        print(f"\n\t\t\tHero's health increased to {hero.health}.\n")

class Armor():
    cost = 20
    name = "armor"  
    def apply(self, hero):
        hero.armor_rating += 2
        if hero.armor_rating >= 6:
            hero.armor_rating = 6
        print(f"\n\t\t\tHero now has armor rating of ({hero.armor_rating}/6)\n")

class Evade():
    cost = 15
    name = "evade"
    def apply(self, hero):
        hero.evasion += 0.15
        evasionChance = hero.evasion*100
        print(f"\n\t\t\tHero now has an evasion chance of {evasionChance}%\n")

class EssenceOfGhost():
    cost = 10
    name = "essence of ghost"
    def apply(self, hero):
        hero.fullevasion = 3
        print(f"\n\t\t\tHero now has 100% evasion for {hero.fullevasion} attacks.\n")

class GreatSword():
    cost = 20
    name = "great sword"
    def apply(self, hero):
        hero.power += 5
        print(f"\n\t\t\tHero now has power of {hero.power}.\n")

class Swap():
    cost = 5
    name = "swap"
    def apply(self, hero, enemy):
        temp = hero.power
        hero.power = enemy.power
        enemy.power = temp
        hero.swapCounter = 1
        print(f"\t\t\tAttacks swapped!\nHero has attack of {hero.power}\nEnemy has attack of {enemy.power}")
    def expire(self, hero, enemy):
        temp = hero.power
        hero.power = enemy.power
        enemy.power = temp
        print(f"\n\t\t\tSwap expired. Attack power returned to normal.\n")
        
class Shop():
    
    items = [Tonic, Sword, SuperTonic, Armor, Evade, EssenceOfGhost, GreatSword, Swap]
    
    def do_shopping(self, hero):
        while True:
            print(f"""
                           .-----.
                         .'       `.
                        :      ^v^  :
                        :           :
                        '           '
         |~        www   `.       .'
        /.\       /#^^\_   `-/\--'
       /#  \     /#%    \   /# \\
      /#%   \   /#%______\ /#%__\\
     /#%     \   |= I I ||  |- |
     ~~|~~~|~~   |_=_-__|'  |[]|
       |[] |_______\__|/_ _ |= |`.
^V^    |-  /= __   __    /-\|= | :;     ===========================
       |= /- /\/  /\/   /=- \.-' :;         Welcome to The Shop
       | /_.=========._/_.-._\  .:'     ===========================
       |= |-.'.- .'.- |  /|\ |.:'
       \  |=|:|= |:| =| |~|~||'|
        |~|-|:| -|:|  |-|~|~||=|      ^V^
        |=|=|:|- |:|- | |~|~|| |
        | |-_~__=_~__=|_^^^^^|/___
        |-(=-=-=-=-=-(|=====/=_-=/\\
        | |=_-= _=- _=| -_=/=_-_/__\ 
        | |- _ =_-  _-|=_- |]#| I II
        |=|_/ \_-_= - |- = |]#| I II
        | /  _/ \. -_=| =__|]!!!I_II!!
       _|/-'/  ` \_/ \|/' _ ^^^^`.==_^.
     _/  _/`-./`-; `-.\_ / \_'\`. `. ===`.
    / .-'  __/_   `.   _/.' .-' `-. ; ====;\\
   /.   `./    \ `. \ / -  /  .-'.' ====='  >
  /  \  /  .-' `--.  / .' /  `-.' ======.' /
                        
                        You have {hero.coins} coins.
                        
                        What do you want to do?
                    """)
            
            for i in range(len(Shop.items)):
                item = Shop.items[i]
                print(f"\t\t\t{i+1}. buy {item.name} ({item.cost})")
                
            print(f"\t\t\t{len(Shop.items) + 1}. leave shop")
            
            try:
                answer = input("> ")
                intAnswer = int(answer)
            except:
                print("\t\t\tInvalid input. Try again.")
                
            if (intAnswer == (len(Shop.items) + 1)):
                break
            elif intAnswer > 0 and intAnswer <= len(Shop.items):
                itemToBuy = Shop.items[intAnswer-1]
                item = itemToBuy()
                if hero.coins >= item.cost:
                    hero.inventory.append(item)
                    hero.buy(hero, item)
                    print(f"\n\t\t\t{(hero.inventory[len(hero.inventory)-1].name).capitalize()} added to inventory.\n")
                else:
                    print("\n\t\t\tNice try. You don't have enough coins.\n")
            elif intAnswer > len(Shop.items):
                print("\t\t\tInvalid input. Try again.")


## main


def main():

    hero = Hero()
    battle_engine = Battle()
    shopping_engine = Shop()

    #randomize this at some point
    enemies = [Goblin(),Zombie(),Shadow(),Medic(),Bard(),Medic(),Behemoth()]

    for enemy in enemies:
            
        
        hero_won = battle_engine.do_battle(hero,enemy)
        
        if not hero_won:
            
            print("""
            _..--""---.
          /           ".
          `            l
          |'._  ,._ l/"\\         ==============================
          |  _J<__/.v._/          |   Rest in peace, brother   |
           \( ,~._,,,,-)          ==============================
            `-\' \`,,j|
               \_,____J
          .--.__)--(__.--.
         /  `-----..--'. j
         '.- '`--` `--' \\
        //  '`---'`  `-' \\
       //   '`----'`.-.-' \\
     _//     `--- -'   \' | \________
    |  |         ) (      `.__.---- -'\\
     \7          \`-(               74\\\\
     ||       _  /`-(               l|//7__
     |l    ('  `-)-/_.--.          f''` -.-"|
     |\     l\_  `-'    .'         |     |  |
     llJ   _ _)J--._.-('           |     |  l
     |||( ( '_)_  .l   ". _    ..__I     |  L
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |
           J  \  /"  (            l       |  |
           | ().'`-()/            |       |  |
          _.-"_.____/             l       l.-l
      _.-"_.+"|                  /        \.  \\
/"\.-"_.-"  | |                 /          \   \\
\_   "      | |                1            | `'|
  |ll       | |                |            i   |
   \\\\       |-\               \j ..          L,,'. `/
 __ \\\\     ( .-\           .--'    ``--../..'      '-..
     `'''`----`\\\\ .....--'''
                \\\\    

                """)
            
            break
        
        if(enemy.name == "behemoth" and enemy.alive() == False):
            print("\n\t\t\t******************************************************************************\n")
            print(f"\t\t\tCongratulations! You've won! Take those {hero.coins} coins home with you!")
            print("\n\t\t\t******************************************************************************\n")
            break
        
        if(enemy.name == 'zombie'):
            hero.coins += 5
        
        shopping_engine.do_shopping(hero)
        
main()
