km = int(input('\033[1;33mQUAL A VELOCIDADE ATUAL DO CARRO? '))
if km > 80:
    mult = (km - 80)
    print('\033[1;31mVocê ultrapassou do limite.\n'
          'sua multa será de: {}R${:.2f}{}'.format( '\033[32m', mult * 7.00, '\033[m'))
    print('\033[1;36mOBRIGADO! DIRIJA COM SEGURANÇA!')
else:
    print('\033[32mTudo tranquilo! Você não passou do limite, parabéns!')
