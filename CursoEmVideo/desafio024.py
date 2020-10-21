'''
Crie um programa que leia o nome de uma cidade 
diga se ela começa ou não com o nome "SANTO".
'''

name = str(input('Digite o nome da sua cidade: '))
name = name.upper().strip().split()
print(name[0] == 'SANTO')
