'''
Escreva um programa que leia um valor em metros, e o exiba convertido em centímetros e milímetros
'''

#Entrada
dmetros = float(input('Uma distância em metros: '))

#Processamento/Saída
print('A medida de {:.2f}m corresponde a'.format(dmetros))
print('{}km'.format(dmetros/1000))
print('{}hm'.format(dmetros/100))
print('{}dam'.format(dmetros/10))
print('{}m'.format(dmetros/1))
print('{}dm'.format(dmetros*10))
print('{}cm'.format(dmetros*100))
print('{}mm'.format(dmetros*1000))
