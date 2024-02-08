# Projeto 2 - Chute um número
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o 
usuário chute um número até que o valor aleatório gerado no início do programa seja 
chutado corretamente. 

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado
no início do programa.

# Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue
mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- valor aleatório de 1 a 10
- chute do usuário
2. O que devo fazer com estes dados?
- Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no inicio do programa e 
dizer se o chute foi maior, menor ou igual ao valor que foi gerado
3. Quais são as restrições deste problema?
- Um valor aleatório de 1 a 10
4. Qual é o resultado esperado?
-programa dizer se o chute foi maior, menor ou igual ao valor que foi gerado
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?

#pseudocodigo
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
  print ('Chute foi maior que o valor gerado.')
if chute < valor_aleatorio:
  print ('Chute foi menor que o valor gerado.')
if chute = valor_aleatorio:
  print ('Você acertou!')
'''
# chamar uma biblioteca 

import random 

valor_aleatorio = random.randint(1, 10)
acertou = False
while acertou == False:
  chute = int(input ('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute foi maior que o valor gerado.')
  elif chute < valor_aleatorio:
    print ('Chute foi menor que o valor gerado.')
  elif chute == valor_aleatorio:
    acertou = True
    print ('Você acertou!')

#uso do laço while para que o usuario possa fazer mais de 1 chute até acertar