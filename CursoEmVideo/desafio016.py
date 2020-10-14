'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre em sua tela a sua
porção inteira

Ex.: Digite um número: 6.127
     O número 6.127 tem a parte inteira 6
'''

from math import trunc

n1 = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n1, trunc(n1)))
