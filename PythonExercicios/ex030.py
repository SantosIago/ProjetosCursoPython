from time import sleep
num = int(input('Digite um número qualquer: '))
res = num % 2
print('PROCESSANDO...')
sleep(3)
if res == 0:
    print('ESSE NÚMERO É PAR!')
    print('--' * 10)
else:
    print('ESSE NÚMERO É IMPAR!')
    print('--' * 10)