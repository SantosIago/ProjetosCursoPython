from random import randint
from time import sleep

ale = randint(0,5)# Faz o computador "PENSAR"
print("-=-" * 20)
print("Vou pensar em um número, entre 0 a 5. Tente Adivinhar...")
print("-=-" * 20)
num = int(input("Em qual número eu pensei? ")) # O jogador deverá adivinhar
print('\033[34mPROCESSANDO...\033[m')
sleep(3)
if num == ale: # Se o jogador acertar o número pensado
    print('\033[32mPARABÉNS! VOCÊ CONSEGUIU ACERTAR! :)')
else: # Se caso o jogador não acertar o número pensado
    print('\033[31mQUE PENA! VOCÊ ERROU, NÃO PENSEI EM {}, PENSEI EM {}'.format(num, ale))