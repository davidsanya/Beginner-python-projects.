# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:36:01 2024

@author: davidsanya
"""
import random 
print("welcome to the Number Guessing Game!\n\nI'm thinking of a number between 1 and 100")
print("\nplease select the difficulty level\n\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances) ")
def game():
    choice=input("\nEnter your choice: ")
    
    computerguess=random.randint(1,100)
   
    
    if choice==1 or choice=="1":
        for i in range(10):
            playerguess=input("Enter your guess: ")
            makeinteger=int(playerguess)
            if makeinteger == computerguess:
                print("you win")
                break 
                playagain=input("would you like to play again yes/no:")
                if playagain=="yes"and "YES":
                    game()
            elif makeinteger>computerguess:
             print(f"incorrect! the number is less than {makeinteger}")
            elif makeinteger<computerguess:
                print(f"incorrect! the number is greater that {makeinteger}")
        else:
            print("you lose")
            playagain=input("would you like to play again yes/no:")
            if playagain=="yes"and "YES":
                game()
            
    if choice==2 or choice=="2":
        for i in range(5):
            playerguess=input("Enter your guess: ")
            makeinteger=int(playerguess)
            if makeinteger == computerguess:
                print("you win")
                break 
                playagain=input("would you like to play again yes/no:")
                if playagain=="yes"and "YES":
                    game()
                elif makeinteger>computerguess:
                 print(f"incorrect! the number is less than {makeinteger}")
                elif makeinteger<computerguess:
                  print(f"incorrect! the number is greater that {makeinteger}")
        else:
            print("you lose")
            playagain=input("would you like to play again yes/no:")
            if playagain=="yes"and "YES": 
                game()
            
    if choice==3 or choice=="3":
        for i in range(3):
            playerguess=input("Enter your guess: ")
            makeinteger=int(playerguess)
            if makeinteger == computerguess:
                print("you win")
                break 
                playagain=input("would you like to play again yes/no:") 
                if playagain=="yes"and "YES":
                    game()
                elif makeinteger>computerguess:
                   print(f"incorrect! the number is less than {makeinteger}")
                elif makeinteger<computerguess:
                      print(f"incorrect! the number is greater that {makeinteger}")
        else:
            print("you lose") 
            playagain=input("would you like to play again yes/no:")
        if playagain=="yes"and "YES":
            game()
        
    
game()

        
        
        

            
        
        
        
        
