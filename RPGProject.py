import random
import sys
import time


#print with a typewriter effect
def slow_print(text, delay=0.001):

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


#character class details
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def is_alive(self):
        return self.hp > 0


#battle method for battling enemies
def battle(player, enemy):

    slow_print(f"\n⚔️ A wild {enemy.name} appears!")
    
    while player.is_alive() and enemy.is_alive():
        
        #player stats and choices shown
        slow_print(f"\n{player.name} HP: {player.hp}/{player.max_hp} | {enemy.name} HP: {enemy.hp}/{enemy.max_hp}")
        slow_print("Choose your action:")
        slow_print("1. Attack")
        slow_print("2. Block")
        slow_print("3. Heal")

        choice = input("> ").strip()

        #attack
        if choice == "1":  
            dmg = random.randint(5, 15)
            enemy.hp -= dmg
            slow_print(f"You slash the {enemy.name} for {dmg} damage!")

        #block
        elif choice == "2":  
            slow_print("You brace for an attack, reducing incoming damage...")

        #heal   
        elif choice == "3":  
            heal = random.randint(8, 18)
            player.hp = min(player.max_hp, player.hp + heal)
            slow_print(f"You healed for {heal} HP!")

        #incorrect input
        else:
            slow_print("You hesitate and lose your turn!")


        if enemy.is_alive():
            
            enemy_attack = random.choice(["attack", "heavy", "miss"])

            #enemy attack with your block benefit
            if choice == "2" and enemy_attack == "attack":
                dmg = max(0, random.randint(5, 10) - random.randint(5, 10))
                slow_print(f"The {enemy.name} attacks, but your block reduces it to {dmg} damage!")

            #attacks
            elif enemy_attack == "attack":
                dmg = random.randint(5, 10)
                player.hp -= dmg
                slow_print(f"The {enemy.name} hits you for {dmg} damage!")
            
            elif enemy_attack == "heavy":
                dmg = random.randint(8, 15)
                player.hp -= dmg
                slow_print(f"The {enemy.name} smashes you with a heavy attack for {dmg} damage!")
            
            elif enemy_attack == "miss":
                slow_print(f"The {enemy.name} misses its attack!")

    if player.is_alive():
        slow_print(f"\n🎉 You defeated the {enemy.name}!")

    else:
        slow_print("\n💀 You have fallen in battle...")
        sys.exit()



#main adventure body
def adventure():
    
    player = Character("Hero", 50)
    slow_print("🌟 Welcome, Hero! Your quest begins...\n")

    #while player is alive or "continue" = 2 (to not continue)
    while True:
        slow_print("\nYou arrive at a crossroads. Where will you go?")
        slow_print("1. Venture into the dark forest 🌲")
        slow_print("2. Explore the abandoned village 🏚️")
        slow_print("3. Enter the mysterious cave ⛰️")
        slow_print("4. Rest at the campfire 🔥 (recover health)")

        choice = input("> ").strip()

        if choice == "1":
            battle(player, Character("Goblin", 30))

        elif choice == "2":
            battle(player, Character("Bandit", 35))
        
        elif choice == "3":
            battle(player, Character("Cave Beast", 40))
        
        elif choice == "4":
            heal = random.randint(10, 20)
            player.hp = min(player.max_hp, player.hp + heal)
            slow_print(f"You rest and regain {heal} HP. Feeling refreshed!")

        #incorrect input
        else:
            slow_print("You wander aimlessly... try choosing a path.")

        if not player.is_alive():
            slow_print("The adventure ends here.")
            break

        slow_print("\nDo you wish to continue your journey?")
        slow_print("1. Yes, onward!")
        slow_print("2. No, end the adventure.")

        cont = input("> ").strip()
        if cont == "2":
            slow_print("You decide to end your journey. Farewell, Hero!")
            break

#execute main code body
if __name__ == "__main__":
    adventure()
