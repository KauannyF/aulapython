"""
 Comandos condicionais .. são comandos que efetuam desvios no fluxo do programa

Comando if...- SE alguma coisa for verdadeira faça isto, caso contrário faça a opção de negação

SINTAXE python:
Print(conteúdo)
if teste-condicional
    faça algo


Sintaxe do php
if (teste condicional) {
faça algo;
}
 """
idade = 15
if idade >= 18:
    print("Você é maior de idade")
else:
    print("você é menor vá para a disney")

"""
Um parque de diversões que cobre preços diferentes para grupos etários
 4 anos entrada gratuita
entre 4 a 18 custa R$ 5,00
Acima de 18 custa R$ 20,00


if teste condicional:
    resp condicional1
elif teste condicional2:                                                       - ELSE IF
    resp condicional2
elif teste condicional3:
    resp condicional3
else:
    resposta falsa geral
"""

idade = 17
if idade <= 4:
   print("gratuito")
elif idade <18:
    print("Custa R$5,00")
else:
    print("Custa R$20,00")


idade2 = 12
if idade2 <=4:
    preco = 0
elif idade2<18:
    preco = 5
else:
    preco = 20

print("Sua entrada custará R$", preco)

"""
Crie um algoritmo que receba 3 notas, calcule a média (n1+n2+n3)/3
e se a média for maior que 7 exibir a mensagem "aprovado" caso contrário "reprovado"
"""


N1 = 7
N2 = 0
N3 = 7
media = (N1+N2+N3)/3

if media <=4.0 and media >= 0:
    print("reprovado")
elif media >= 4.1 and media <= 5.9:
    print("recuperação")
else:
    print("aprovado")


