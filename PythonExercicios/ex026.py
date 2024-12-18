frase = str(input('Digite a frase: ')).lower().strip()
print('Quantidade de vezes que a letra "A" aparece: {}'.format(frase.count('a')))
print("A primeira letra A aparece na posição {}".format(frase.find('a')+1))
print("A ultima letra A apareceu na posição {}".format(frase.rfind('a')+1))