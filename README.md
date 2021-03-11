# Jogo da velha - c/ computador
<h5>Gessyca Moreira<h5>

<h4> Para criar esse código ultilizamemos a biblioteca de gerador de números aleatórios <i>RANDOM<i>
 Usaremos o random.randint(a, b), para retornarmos um inteiro aleatório N de forma que a <= N <= b.<h4>
  
```
import random 

escolha = int(input("\n 1 - Pedra\n 2- Papel\n 3 - Tesoura\n Sua escolha é? "))
computador = random.randint(1, 3)
    
if escolha > 3 or escolha < 0:
    print ("\nOperação invalida")
        
elif escolha == 1:
    if computador == 1:
        print(f"\nEmpate\nEssa foi a escolha do computador: {computador}")
    elif computador == 2 :
        print(f"\nVitoria do Computador\nEssa foi a escolha do computador: {computador}")
    elif computador == 3:
        print(f"\nVitoria do Usuario\nEssa foi a escolha do computador: {computador}")
            
elif escolha == 2:
    if computador == 1:
        print(f"\nVitoria do Usuario\nEssa foi a escolha do computador: {computador}")
    elif computador == 2 :
        print(f"\nEmpate\nEssa foi a escolha do computador: {computador}")
    elif computador == 3:
        print(f"\nVitoria do Computador\nEssa foi a escolha do computador: {computador}")

elif escolha == 3:
    if computador == 1:
        print(f"\nVitoria do Computador\nEssa foi a escolha do computador: {computador}")
    elif computador == 2 :
        print(f"\nVitoria do Usuario\nEssa foi a escolha do computador: {computador}")
    elif computador == 3:
        print(f"\nEmpate\nEssa foi a escolha do computador: {computador}") 
```
