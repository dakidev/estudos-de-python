#!/usr/bin/env python3
import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

nr = random.randrange(0, 5) #nr = o número sorteador

n1 = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if n1 == nr:
    print('Parabéns, você acertou!')
else:
    print('Eu ganhei! Pensei no {} e não no {}'.format(nr, n1))

