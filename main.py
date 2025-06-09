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
    print("C Choose Pokemon")
    print("S Single Player")
    print("M Multiplayer")
    print("B Buy cards")
    print("Q Quit")
    print()

def InputChoose_Pokemon():
    choose_pokemon = input("Please Choose your Pokemon (Pikachu): ")
    return choose_pokemon

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
            "attack": 20,
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
            print("Why'd sleep you lazy bum?")
        elif action == "gnaw":
            rival["health"] -= player["gnaw"]
            print(f"You attacked! Rival's health is now {rival['health']}")
        else:
            print("Unknown action.")
        if rival["health"] > 0:
            player["health"] -= rival["attack"]
            print(f"Charmander attacks! Your health is now {player['health']}")
    if player["health"] > 0:
        print("You win!")
    else:
        print("You lost!")


    def Multiplayer():
        player = get_player(chosen_pokemon)
        

def Main():
    menu_option = ""
    chosen_pokemon = "Pikachu"  # Default
    while menu_option != "Q":
        DisplayMenu()
        menu_option = input("Enter Option > ").upper()
        if menu_option == "C":
            chosen_pokemon = InputChoose_Pokemon()
        elif menu_option == "S":
            Single_player(chosen_pokemon)
        elif menu_option == "Q":
            print("Goodbye!")

Main()