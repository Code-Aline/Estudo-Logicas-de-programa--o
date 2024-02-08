# Projeto 3 - Medidor de Velocidade
'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa leve, grave ou gravissima. 
Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade maxima, exibir: "Levou multa grave", e caso esteja acima de 20km da velocidade maxima, exiba: "levou multa gravissima."

# Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue
mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
-velocidade
2. O que devo fazer com estes dados?
-Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade maxima, exibir: "Levou multa grave", e caso esteja acima de 30km da velocidade maxima, exiba: "levou multa gravissima."
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
-Exibir se a pessoa levou multa ou não
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?

#pseudocodigo
velocidade_permitida = 80km
velocidade = int (input =('Digite a velocidade: '))

if velocidade <= velocidade_permitida 
print ('Não houve multa')
if velocidade > velocidade_permitida e velocidade < = velocidade_maxima + 10km 
  print ('leve')
if velocidade > velocidade_permitida +11 e velocidade < = velocidade_maxima + 20
  print ('grave')
if velocidade < velocidade_permitida +20:
  print ('gravissima')
'''

velocidade_permitida = 80
velocidade = int(input ('Digite a velocidade: '))
if velocidade <= velocidade_permitida:
  print ('Não houve multa')
elif velocidade > velocidade_permitida and velocidade <= velocidade_permitida + 10:
  print ('leve')
elif velocidade >= velocidade_permitida + 11 and velocidade <= velocidade_permitida + 20:
  print ('grave')
elif velocidade > velocidade_permitida + 20:
  print ('gravissima')