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

def rival():
   bad_guy = "Pikachu"
   Health = 100
   Energy = 3
   Attack = 20
   Sleep = 2


def Single_player():
   if InputChoose_Pokemon == "Pikachu":
      Health = 100
      Energy = 3
      Attack = 20
      Sleep = 2
      while Health > 0:
         print("Your rival is {}".format(rival))
         Action = input("What do you want to do")
         if Action == "Attack":
            rival.health -= 20
         
          
       


def Main():

    MenuOption = ""  

    while MenuOption != "Q":
        DisplayMenu()
        MenuOption = input("Enter Option > ").upper()
        if MenuOption == "C":
            Choose_Pokemon = InputChoose_Pokemon()
        elif MenuOption == "S":
           Single_player()
            
      
Main()
      








   


















