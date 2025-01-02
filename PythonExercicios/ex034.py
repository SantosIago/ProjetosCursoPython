sal = float(input('Digite o seu salário: R$'))
if sal > 1250.00:
    aumento = sal * (10/100) + sal
    print('Seu salario era {:.2f}. Foi aumentado para {:.2f}!'.format(sal, aumento ))
else:
    aumento = sal * (15/100) + sal
    print('Seu salario era R${:.2f}. Foi aumentado para R${:.2f}'.format(sal, aumento))
