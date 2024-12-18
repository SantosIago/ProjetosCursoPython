sal = float(input('O seu salário é de: R$'))
novo = sal + (sal * 15 / 100)
print('Seu salário que era de R${}, sofreu aumento de 15%, agora seu salário é de R${:.2f}.'.format(sal, novo))
