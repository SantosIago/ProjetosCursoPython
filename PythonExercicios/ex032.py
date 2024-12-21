ano = int(input('Por favor! Digite o ano desejado: '))
bis = ano % 4
if bis == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')
