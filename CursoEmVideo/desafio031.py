#!/usr/bin/env python3

# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('Qual é a distância da sua viagem? '))

if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print('O total a pagar é R${:.2f}, tenha uma boa viagem!'.format(valor))

