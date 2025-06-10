import pokemon
import random


print("""
                                 ,'\ 
    _.----.        ____         ,'  _\   ___    ___     ____ 
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`. 
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  | 
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  | 
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  | 
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     | 
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    | 
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   | 
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   | 
        \_.-'       |__|    `-._ |              '-.|     '-.| |   | 
                                `'                            '-._| """)


def DisplayMenu():
    print()
    print("1 Choose First Pokemon")
    print("2 Choose Second Pokemon")
    print("S Single Player")
    print("M Multiplayer")
    print("B Buy cards")
    print("Q Quit")
    print()

def InputChoose_Pokemon():
    choose_pokemon = input("Please Choose your Pokemon (Pikachu): ")
    return choose_pokemon

def InputChoose_Pokemon2():
    choose_pokemon2 = input("Please Choose your Pokemon (Pikachu): ")
    return choose_pokemon2

def get_rival():
    return {
        "name": "Charmander",
        "health": 230,
        "energy": 3,
        "attack": 20,
        "sleep": 2
    }

def get_player(pokemon_name):
 
    if pokemon_name.lower() == "pikachu":
        return {
            "name": "Pikachu",
            "health": 100,
            "energy": 3,
            "attack": 30,
            "gnaw": 60,
            "sleep": 2
        }
    else:
        print("Unknown Pokemon, defaulting to Pikachu.")
        return {
            "name": "Pikachu",
            "health": 100,
            "energy": 3,
            "attack": 20,
            "gnaw": 60,
            "sleep": 2
        }
    
def get_player2(pokemon_name2):
 
    if pokemon_name2.lower() == "pikachu":
        return {
            "name": "Pikachu",
            "health": 100,
            "energy": 3,
            "attack": 30,
            "gnaw": 60,
            "sleep": 2
        }
    else:
        print("Unknown Pokemon, defaulting to Pikachu.")
        return {
            "name": "Pikachu",
            "health": 100,
            "energy": 3,
            "attack": 20,
            "gnaw": 60,
            "sleep": 2
        }
    


def Single_player(chosen_pokemon):
    player = get_player(chosen_pokemon)
    rival = get_rival()
    print(f"Your rival is {rival['name']}!")
    while player["health"] > 0 and rival["health"] > 0:
        print(f"\nYour Health: {player['health']} | Rival Health: {rival['health']}")
        action = input("What do you want to do? (attack🗡️/gnaw💫/sleep😴): ").strip().lower()
        if action == "attack":
            rival["health"] -= player["attack"]
            print(f"You attacked! Rival's health is now {rival['health']}")
        elif action == "sleep":
            print("Gained energy for sleeping")
            player["energy"] += player["sleep"]
            print(f"You slept! Your energy is now {player['energy']}")
        elif action == "gnaw":
            if player["energy"] > 0:  # Fixed the condition to check player's energy
                rival["health"] -= player["gnaw"]
                player["energy"] -= 1
                print(f"You attacked! Rival's health is now {rival['health']}")
                print(f"You used energy! Your energy is now {player['energy']}")
            else:
                print("Not enough energy")

        else:
            print("Unknown action.")
        if rival["health"] > 0:
            player["health"] -= rival["attack"]
            print(f"Charmander attacks! Your health is now {player['health']}")
    if player["health"] > 0:
        print("You win!")
    else:
        print("You lost!")


def Multiplayer(chosen_pokemon, chosen_pokemon2):
    player = get_player(chosen_pokemon)
    player2 = get_player2(chosen_pokemon2)
    turn = 1
    while player["health"] > 0 and player2["health"] > 0:
        if player["health"] > 0 and turn == 1:
            print(f"\nPlayer 1 Health: {player['health']} | Player 2 Health: {player2['health']}")
            action1 = input("What do you want to do? (attack🗡️/gnaw💫/sleep😴): ").strip().lower()
            if action1 == "attack":
                player2["health"] -= player["attack"]
                print(f"You attacked! Player 2's health is now {player2['health']}")
                turn +=1
            elif action1 == "sleep":
                print("Gained energy for sleeping")
                player["energy"] += player["sleep"]
                print(f"You slept! Your energy is now {player['energy']}")
                turn += 1
            elif action1 == "gnaw":
                if player["energy"] > 0:  # Fixed the condition to check player's energy
                    player2["health"] -= player["gnaw"]
                    player["energy"] -= 1
                    print(f"You attacked! Rival's health is now {player2['health']}")
                    print(f"You used energy! Your energy is now {player['energy']}")
                    turn +=1
            else:
                print("Not enough energy")
                turn += 1
        else:
            ("Unknown Action.")
            turn += 1

        if player2["health"] > 0 and turn == 2:
            action2 = input("What do you want to do, Player 2? (attack🗡️/gnaw💫/sleep😴): ").strip().lower()
            if action2 == "attack":
                player["health"] -= player2["attack"]
                print(f"You attacked! Player 1's health is now {player['health']}")
                turn -= 1
            elif action2 == "sleep":
                print("Gained energy for sleeping, Player 2")
                player["energy"] += player2["sleep"]
                print(f"You slept! Your energy is now {player2['energy']}")
                turn -= 1
            elif action2 == "gnaw":
                if player2["energy"] > 0:  # Fixed the condition to check player's energy
                    player["health"] -= player2["gnaw"]
                    player2["energy"] -= 1
                    print(f"You attacked! Player 1's health is now {player['health']}")
                    print(f"You used energy! Your energy is now {player2['energy']}")
                    turn -= 1
            else:
                print("Not enough energy")
                turn -= 1
        else:
            ("Unknown Action.")
            turn -= 1


    if player["health"] > 0:
        print("Player 1 wins")
    else:
        print("Player 2 wins")


def buy_cards():
    

    Gatcha = ["Pikachu - Common", "Charmander - Rare", "Isagi - Ultra Rare", "Chigiri - Legendary"]
    print(Gatcha)
    x = random.choice(Gatcha)
    buy = 0
    while buy == 0:
        purchase = input("would you like to buy a card (Y/N)")
        if purchase == "Y":
            print(x)
            buy += 1
        if purchase == "N":
            print("damn...")
            Main()
        
        

def Main():
    menu_option = ""
    chosen_pokemon = "Pikachu"  # Default
    while menu_option != "Q":
        DisplayMenu()
        menu_option = input("Enter Option > ").upper()
        if menu_option == "1":
            chosen_pokemon = InputChoose_Pokemon()
        elif menu_option == "2":
            chosen_pokemon2 = InputChoose_Pokemon2()
        elif menu_option == "S":
            Single_player(chosen_pokemon)
        elif menu_option == "M":
            Multiplayer(chosen_pokemon, chosen_pokemon2)
        elif menu_option == "B":
            buy_cards()
        elif menu_option == "Q":
            print("Goodbye!")

Main()