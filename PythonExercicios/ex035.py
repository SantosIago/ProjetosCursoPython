from time import sleep
print('\033[35m-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20, '\033[m')
l1 = float(input('\033[34mDigite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
print('\033[31mPROCESSANDO...')
sleep(3)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[34mCom os segmentos acima {}PODEM SE FORMAR{}\033[34m um triângulo!'.format('\033[1;32m', '\033[m'))
else:
    print('\033[34mCom os segmentos acima {}NÃO PODEM SE FORMAR{}\033[34m um triângulo!'.format('\033[1;31m', '\033[m'))
