km = int(input('Qual a velocidade atual do carro? '))
if km > 80:
    mult = (km - 80)
    print('Você ultrapassou do limite.\n'
          'sua multa será de: R${:.2f}'.format(km, mult * 7,00))
    print('Obrigado! Dirija com segurança!')
else:
    print('Tudo tranquilo! Você não passou do limite, parabéns!')
