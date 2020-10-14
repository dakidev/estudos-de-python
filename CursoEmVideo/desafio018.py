'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
desse ângulo.
'''

import math

ang = float(input('Digite o ângulo: '))

print('O seno desse ângulo: {}'.format(math.sin(ang)))
print('O cosseno desse ângulo: {}'.format(math.cos(ang)))
print('O tangente desse ângulo: {}'.format(math.tan(ang)))
