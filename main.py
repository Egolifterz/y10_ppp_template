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
    print()

def InputChoose_Pokemon():
   Choose_Pokemon = input("Please Choose your Pokemon (Pikachu): ")
   return Choose_Pokemon


def Single_player():
   if InputChoose_Pokemon == "Pikachu":
      Health = 100
      
       


def Main():

    MenuOption = ""  

    while MenuOption != "Q":
        DisplayMenu()
        MenuOption = input("Enter Option > ").upper()
        if MenuOption == "C":
            Choose_Pokemon = InputChoose_Pokemon()
      
Main()
      








   





main()















