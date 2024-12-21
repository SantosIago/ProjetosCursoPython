print('_____________________________________\n'
      'IMPAR OU PAR?\n'
      '_____________________________________\n')

num = int(input('Digite um número: '))
res = num % 2
if res == 0:
    print('ESSE NÚMERO É PAR!\n'
          '__________________')
else:
    print('ESSE NÚMERO É IMPAR!\n'
          '____________________')