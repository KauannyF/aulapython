# importa biblioteca regex (expressões regulares)
import re

frase = ' O rato roeu a roupa do rei de Roma'

if 'rato' in frase:
    print('palavra encontrada')
    print('ocorre: ', frase.count('rato'))
else:
    print('palavra não encontrada')


mpax = 'o motorista me tratou mal e foi mau-educado na viagem.'\
    'acho que por ser tão mal deve ser punido, me sinto agredida'
if 'mal' in mpax:
    print('palavra encontrada')
    print('ocorre: ', mpax.count('mal'))

else:
    print('não encontrada')

# Ordenação - sort()

print(nomes)
nomes.sort()
print(nomes)
