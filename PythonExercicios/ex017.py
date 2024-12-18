import math
ca = int(input('Qual o valor do cateto adjacente? '))
co = int(input('Qual o valor do cateto oposto? '))
h = math.sqrt(ca**2 + co**2)
print('O triângulo retângulo, com cateto {}cm e {}cm, tem a hipotenusa de {:.2f}cm '.format(ca, co, h))
