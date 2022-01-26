

# Exercício 5

Número = 10
antecessor = Número - 1

if antecessor:
    print("O seu antecessor é", Número - 1)
else:
    print()

"""
Execício 6)
 Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a
área do retângulo. 
"""

a = 5
b = 10
multiplicação= (a*b)

if multiplicação:
    print(a*b, "cm quadrados")
else:
    print()

"""
Exercício 7 
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. 
"""
anos = 19
meses = 4
dias = 21
idadeemdias= (anos * 365) + (meses * 30) + dias
if idadeemdias:
    print(idadeemdias, "é sua idade em dias!")
else:
    print()


"""
exercício 8
Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
de eleitores
"""
Totaldeeleitores= 1000
votosb = 200
votosn = 100
votosv = 700

brancos= (100*votosb)/Totaldeeleitores
nulos = (100*votosn)/Totaldeeleitores
válidos = (100*votosv)/Totaldeeleitores

if brancos:
    print("A porcentagem de votos brancos foi de", brancos, "%")
if nulos:
    print("A porcentagem de votos nulos foi de", nulos, "%")
if válidos:
    print("A porcentagem de votos válidos foi de", válidos, "%")





"""
exercício 9
 Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
Calcular e escrever o valor do novo salário

"""

Salário = 1000
reajuste = 15
novosalário = Salário + (Salário * reajuste/100)
if novosalário:
    print("Esse é seu novo salário R$", novosalário)
else:
    print()

"""
exercício 10
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor
seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro,
calcular e escrever o custo final ao consumidor.
"""
custoF = 1000
imposto = (45*custoF)/100
percentual =(28*custoF)/100
total = custoF+imposto+percentual
if total:
    print("O custo final do carro é de R$", total)
else:
    print()


"""
exercício 11
Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
vendedor. 

"""
Saláriofixo = 1200
carrovendido = 100
Valortotaldasvendas = 15
ValorComissão = 50                                     #Comissão

salario= Saláriofixo + (ValorComissão*carrovendido) + (Valortotaldasvendas*0.05)
if salario:
    print("O salário final é de R$", salario)


"""
exercício 12
 Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
correspondente em graus Celsius (baseado na fórmula abaixo): 

"""
F = 212
celsius = 5 * (F-32)/9

if celsius:
    print(int(celsius), "°C")
else:
    print("fim")


"""
exercício 13
 Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o cálculo da média
final é: 

"""
n1 = 4
n2 = 5
n3 = 6
média= (n1*2+n2*3+n3*5)/10

if média:
    print("média final", média)
else:
    print()
"""
exercício 14
 Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10! 

"""
Valor = 15
if Valor > 10 :
    print("É MAIOR QUE 10!")
elif Valor < 10:
    print("É MENOR QUE 10!")
else:
    print("é provável que seja 10")

"""
exercício 15
 Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo). 

"""
Valor = 6
if Valor >= 0:
    print('Esse número é positivo!')
elif Valor < 0:
    print("Esse número é negativo!")



"""
exercício 16

"""
MaçãsC = 12
MaçãsU = 1.30
MaçãsD = 1.00

unidade= MaçãsU * MaçãsC
Dúzia = MaçãsD * MaçãsC

if unidade < 12:
    print(" Valor da compra é de R$", unidade, "Reais")
elif Dúzia >= 12:
    print("Valor da compra é de R$", Dúzia, "Reais")

"""
exercício 17
 Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever
uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o
aluno é aprovado). Escrever também a média calculada. 
"""
a1 = 10
a2 = 10
média= (a1+a2)/2

if média >= 6:
    print("Aprovado")
elif média < 6:
    print("Reprovado")
"""
exercício 18

"""
nascimento = 2007
subtração = (2022-nascimento)
if subtração >= 16:
    print("Você poderá votar em 2022")
elif subtração < 16:
    print("você não poderá votar em 2022")
else:
    print()
"""
exercício 19
Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles. 
"""
N1 = 60
N2 = 10
if N1 > N2:
    print(N1)
elif N2 > N1:
    print(N2)


"""
exercício 20
 Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente. 
"""

N1 = 10
N2 = 15
if N1 < N2:
    print(N1, N2)
elif N2 < N1:
    print(N2, N1)
else:
    print()
