#!/usr/bin/env python3
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h , mostre uma mensagem dizendo que ele
# foi multado.

# A multa vai custar R$7.00 por cada Km acima do limite

km = float(input('Qual é a velocidade atual do seu carro? '))

if km > 80:
    m = (km - 80) * 7
    print('M U L T A D O! O valor da sua multa é de {}'.format(m))
print('Prontinho! Dirija com SEGURANÇA!')

