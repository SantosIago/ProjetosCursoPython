from time import sleep
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
print('PROCESSANDO...')
sleep(3)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com os segmentos acima PODEM SE FORMAR um triângulo!')
else:
    print('Com os segmentos acima NÃO PODEM SE FORMAR um triângulo!')
