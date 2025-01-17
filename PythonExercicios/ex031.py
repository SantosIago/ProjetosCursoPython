num = float(input('\033[4;34mDigite quantos quilômetros foi a viagem: '))
if num <= 200:
    cobr = num * 0.50
    print('\033[1;37mAo viajar por menos de 200 km, será cobrado R$0,50 por km\n'
          'Com isso, o valor a ser pago será de {}R${}'.format('\033[1;32m', cobr))
else:
    cobr = (num * 0.45)
    print('\033[1;37mAo viajar por mais de 200 km, será cobrado R$0,45 por km\n'
          'Com isso, o valor a ser pago pela viagem será de {}R${}'.format('\033[1;32m', cobr))
