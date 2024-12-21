num = float(input('Digite quantos quilômetros foi a viagem: '))
if num <= 200:
    cobr = num * 0.50
    print('Ao viajar por menos de 200 km, será cobrado R$0,50 por km\n'
          'Com isso, o valor a ser pago será de R${}'.format(cobr))
else:
    cobr = (num * 0.45)
    print('Ao viajar por mais de 200 km, será cobrado R$0,45 por km\n'
          'Com isso, o valor a ser pago pela viagem será de R${}'.format(cobr))
