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
    print("3 Choose Trainer (Buffs)")
    print("S Single Player")
    print("M Multiplayer")
    print("B Buy cards")
    print("Q Quit")
    print()

def InputChoose_Pokemon():
    choose_pokemon = input("Please Choose your Pokemon (Pikachu, Charmander): ")
    return choose_pokemon

def InputChoose_Pokemon2():
    choose_pokemon2 = input("Please Choose your Pokemon (Pikachu, Charmander): ")
    return choose_pokemon2

def InputChoose_trainer():
    choose_trainer = input("Please choose your trainer (Irida)")
    return choose_trainer

def get_rival():
    return {
        "name": "Charmander",
        "health": 50,
        "energy": 3,
        "attack": 30,
        "sleep": 2
    }

def get_player(pokemon_name):
 
    if pokemon_name.lower() == "pikachu":
        return {
            "name": "Pikachu",
            "health": 40,
            "energy": 2,
            "attack": 10,
            "enchanced attack": 30,
            "sleep": 2
        }
    if pokemon_name.lower() == "charmander":
        return {
               "name": "Charmander",
                "health": 50,
                "energy": 2,
                "attack": 10,
                "enchanced attack": 30,
                "sleep": 2
        }


    else:
        print("Unknown Pokemon, defaulting to Pikachu.")
        return {
            "name": "Pikachu",
            "health": 40,
            "energy": 2,
            "attack": 10,
            "enchanced attack": 30,
            "sleep": 2
        }
    

        
def get_player2(pokemon_name2):
 
    if pokemon_name2.lower() == "pikachu":
        return {
            "name": "Pikachu",
            "health": 40,
            "energy": 2,
            "attack": 10,
            "enchanced attack": 30,
            "sleep": 2
        }
    if pokemon_name2.lower() == "charmander":
        return {
               "name": "Charmander",
                "health": 50,
                "energy": 2,
                "attack": 10,
                "enchanced attack": 30,
                "sleep": 2
        }


    else:
        print("Unknown Pokemon, defaulting to Pikachu.")
        return {
            "name": "Pikachu",
            "health": 40,
            "energy": 2,
            "attack": 10,
            "enchanced attack": 30,
            "sleep": 2
        }
    

        
    








def get_trainer(trainer_name):
    if trainer_name.lower() == "irida":
        return {
            "name": "Irida",
            "healing": 40
        }

    


        

    


def Single_player(chosen_pokemon, chosen_trainer):
    player = get_player(chosen_pokemon)
    trainer = get_trainer(chosen_trainer) # procedures return None   ... whereas functinos must RETURN a result
    rival = get_rival()
    print(f"Your rival is {rival['name']}!")
    while player["health"] > 0 and rival["health"] > 0:
        print(f"\nYour Health: {player['health']} | Rival Health: {rival['health']}")
        action = input("What do you want to do? (attack🗡️/enchanced attack💫/sleep😴/trainer skill💡): ").strip().lower()
        if action == "attack":
            rival["health"] -= player["attack"]
            print(f"You attacked! Rival's health is now {rival['health']}")
        elif action == "sleep":
            print("Gained energy for sleeping")
            player["energy"] += player["sleep"]
            print(f"You slept! Your energy is now {player['energy']}")
        elif action == "enchanced attack":
            if player["energy"] > 0:  # Fixed the condition to check player's energy
                rival["health"] -= player["enchanced attack"]
                player["energy"] -= 1
                print(f"You attacked! Rival's health is now {rival['health']}")
                print(f"You used energy! Your energy is now {player['energy']}")
            else:
                print("Not enough energy")
        elif action == "trainer skill":
            player["health"] += trainer["healing"]
            print(f"Trainer uses skill! Your health is now {player['health']}")

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
            action1 = input("What do you want to do? (attack🗡️/enchanced_attack💫/sleep😴): ").strip().lower()
            if action1 == "attack":
                player2["health"] -= player["attack"]
                print(f"You attacked! Player 2's health is now {player2['health']}")
                turn +=1
            elif action1 == "sleep":
                print("Gained energy for sleeping")
                player["energy"] += player["sleep"]
                print(f"You slept! Your energy is now {player['energy']}")
                turn += 1
            elif action1 == "enchanced_attack":
                if player["energy"] > 0:  
                    player2["health"] -= player["enchanced attack"]
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
            action2 = input("What do you want to do, Player 2? (attack🗡️/enchanced attack💫/sleep😴): ").strip().lower()
            if action2 == "attack":
                player["health"] -= player2["attack"]
                print(f"You attacked! Player 1's health is now {player['health']}")
                turn -= 1
            elif action2 == "sleep":
                print("Gained energy for sleeping, Player 2")
                player["energy"] += player2["sleep"]
                print(f"You slept! Your energy is now {player2['energy']}")
                turn -= 1
            elif action2 == "enchanced attack":
                if player2["energy"] > 0:  # Fixed the condition to check player's energy
                    player["health"] -= player2["enchanced attack"]
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
        elif menu_option == "3":
            chosen_trainer = InputChoose_trainer()
        elif menu_option == "S":
            Single_player(chosen_pokemon,chosen_trainer)
        elif menu_option == "M":
            Multiplayer(chosen_pokemon, chosen_pokemon2)
        elif menu_option == "B":
            buy_cards()
        elif menu_option == "Q":
            print("Goodbye!")

Main()