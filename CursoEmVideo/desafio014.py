'''
Escreva um programa que converta um temperatura digita em ºC para ºF.
'''

#Entrada
c = float(input('Informe a temperatura em ºC: '))

#Processamento
#0ºC = 32ºF
f = (c * 9/5) + 32

#saída
print('A temperatura de {}ºC coresponde a {}ºF!'.format(c, f))
