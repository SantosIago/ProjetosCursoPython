from random import randint

ale = randint(0,5)
num = int(input('Pensei em um número de 0 a 5. Diga, que número pensei: '))
if num == ale:
    print('---------------------------------')
    print('Parabéns! Você venceu! :)')
    print('---------------------------------')
else:
    print('---------------------------------')
    print('Que mancada! Você errou, meu número foi {}!'.format(ale))
    print('---------------------------------')