nome = str(input('Nome completo: '))
quantidade = nome.count(' ')
div_nome = nome.split()
primeiro_nome = div_nome[0]

print('Nome em letra maiúscula: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras tem: {}'.format(len(nome) - quantidade))
print('Quantas letras tem o primeiro nome: {}'.format(len(primeiro_nome)))
