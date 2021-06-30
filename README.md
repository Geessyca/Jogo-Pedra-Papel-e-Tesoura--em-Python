<h1 align="center">
  🎓<br>Jogo Pedra, Papel e Tesoura
</h1>
 
<h4 align="center">
  O intuito deste repositório é compartilhar a construção um Jogo de Pedra, Papel e Tesoura construida em Python.
</h4>

<h2 align="left">
  Passo a passo ↷ 
</h2>

 
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
                              
                              
##  👩🏻‍💻 Autora<br>
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/geessyca">
        <img src="https://avatars.githubusercontent.com/u/72661229?v=4" width="100px;" alt="Icon GitHub"/><br>
        <sub>
          <b>Gessyca Moreira</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
