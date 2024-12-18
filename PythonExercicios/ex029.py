print('____________________________________________________\n'
      'Seja bem-vindo(a) a consulta de multa por kilometros\n'
      'O valor máximo de kilometragem é de 80km/h\n'
      '\n'
      'Ao passar, será cobrado R$7,00 por cada km acima\n'
      'do limite\n'
      '_____________________________________________________')

km = int(input('Digite a kilometragem que o carro percorreu: '))
if km > 80:
    mult = (km - 80)
    print('__________________________________________\n'
          'Perdão, mas você passou do limite\n'
          'Você andou {}km/h, com isso será multado\n'
          'E sua multa será de: R${:.2f}'.format(km, mult * 7,00))
else:
    print('____________________________________________________\n'
          'Tudo tranquilo! Você não passou do limite, parabéns!')
