# Declaração de uma lista (Nas outras líguagens chama se ARRAY - Vetor)
nomes = ['juan', 'kauanny', 'jorge', 'diogo', 'rafael', 'eduardo']
idades = [46, 18, 38, 30, 43, 38]
print(nomes)
print(idades)

# Listar um único elemento da lista
print(nomes[2].title())
print(nomes[0].title())
print(nomes[-1])

# Concatenar valores da lista
mensagem = "O aluno da posição 3 é o "+nomes[3].title()+"e a sua idade é:", idades[3]
print(mensagem)

#Alterar valor da lista
motos = ['honda', 'yamaha', 'kawasaki']
print(motos)
motos[0] ='ducati'
print(motos)

#Acrescetar valores ao final da lista a lista - append (conteúdo)
motos.append('honda')
print(motos)
print(motos[3])

#Inserir novos elementos na lista em posição determinada

frutas = ['banana', 'maçã', ' laranja']
frutas.insert(0, 'pera')
print(frutas)

#Apagar um elemento da lista

del frutas[1]
print(frutas)

carros = ['Ford', 'BMW', 'Toyota']
print(carros)

del carros[0]
print(carros)

carros.insert( 0,'Ford')
print(carros)

# Ordenação - sort() modifica a posição dos elementos dentro da lista

#print(nomes)
#nomes.sort()
#print(nomes)

#ordenar a lista sem alterar a listagem original
print('lista original')
print(nomes)
print('Lista ordenada temporariamente')
print(sorted(nomes))
print(nomes)

#ordem reversa
print('Ordem inversa de apresentação')
nomes.reverse()
print(nomes)

#tamanho da   lenght (tamanho)
print("tamanho da lista: ", len(nomes))

#criando listas numéricas
# range()


# Loop infinito
número = 5
while número <= 5:
    print(número)
