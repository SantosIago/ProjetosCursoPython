a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
# Verificando quem é o maior
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
