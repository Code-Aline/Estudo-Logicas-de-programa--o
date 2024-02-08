# Coleções (listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
# Lista
precos = [20,50,200]
#          0, 1, 2   Ex de lista e chamada de um item
print (precos [0])
# Para descobrir o indice de um item da lista
print (precos.index(200))

# Lista
diversidades = [15,'Jhonatan',True]
print (diversidades [0])
print (diversidades [1])
print (diversidades [2])

#laços em iteráveis
for preco in precos: 
  print (preco)

''' Exemplo 5 - Some os valores (exemplo com coleções) 
Dados uma coleção de dados "idades" [15,46,75,34,23],
imprima na tela a soma destes valores 

idades = [15,46,75,34,23]
total = 0
loop idade em idades
total = total + idade
print total
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
  total = total + idade
print (total)