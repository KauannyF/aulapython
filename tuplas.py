#Tupla são criadas e não podem ser modificadas em tempo de execução.
dimensoes = (200, 50, 30, 58, 70)
print(dimensoes[0])
print(dimensoes[1])
#dimensoes[0 = 400
#print(dimensoes[0])

print('-------')
print("percorrendo elementos da tupla")
for dimensao in dimensoes:
    print(dimensao)
#lista
"""
nome = [200, 20]
print(nome[0])
print(nome[1])
"""

for d in dimensoes:
    print(d)

print ("conteúdo t1")
t1 = (1,)
print(t1[0])

lista = list(t1)
print(lista[0], type(lista))
lista[0] = 2
print(lista[0])

tupla = tuple(lista)
print(tupla[0])

#olá
