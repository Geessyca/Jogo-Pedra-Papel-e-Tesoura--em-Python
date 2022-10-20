#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 

userChoice = int(input("\n 1 - Pedra\n 2- Papel\n 3 - Tesoura\n Sua escolha é? "))
randomChoice = random.randint(1, 3)
    
if userChoice > 3 or userChoice < 0:
    print ("\nOperação invalida")
        
elif userChoice == 1:
    if randomChoice == 1:
        print(f"\nEmpate\nEssa foi a escolha do computador:{randomChoice}")
    elif randomChoice == 2 :
        print(f"\nVitoria do Computador\nEssa foi a escolha do computador:{randomChoice}")
    elif randomChoice == 3:
        print(f"\nVitoria do Usuario\nEssa foi a escolha do computador:{randomChoice}")
            
elif userChoice == 2:
    if randomChoice == 1:
        print(f"\nVitoria do Usuario\nEssa foi a escolha do computador:{randomChoice}")
    elif randomChoice == 2 :
        print(f"\nEmpate\nEssa foi a escolha do computador:{randomChoice}")
    elif randomChoice == 3:
        print(f"\nVitoria do Computador\nEssa foi a escolha do computador:{randomChoice}")

elif userChoice == 3:
    if randomChoice == 1:
        print(f"\nVitoria do Computador\nEssa foi a escolha do computador:{randomChoice}")
    elif randomChoice == 2 :
        print(f"\nVitoria do Usuario\nEssa foi a escolha do computador:{randomChoice}")
    elif randomChoice == 3:
        print(f"\nEmpate\nEssa foi a escolha do computador: {randomChoice}") 
