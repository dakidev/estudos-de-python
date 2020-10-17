'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

n1 = input('Primeiro(a) aluno(a): ')
n2 = input('Segundo(a) aluno(a): ')
n3 = input('Terceiro(a) aluno(a): ')
n4 = input('Quarto(a) aluno(a): ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de aprensentação será: ')
print(lista)
