'''
Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações
possíveis sobre ele
'''
#Entrada

n1 = input('Digite algo: ')

#processamento/saída
print('sua classe é:{}'.format(type(n1)))
print(f'ele só tem espaços? {n1.isspace()}')
print(f'é um número? {n1.isnumeric()}')
print(f'é alfabético? {n1.isalpha()}')
print(f'é alfanumérico? {n1.isalnum()}')
print(f'está em maiuscúlas? {n1.isupper()}')
print(f'está em minúsculas? {n1.islower()}')
print(f'está capitalizado? {n1.istitle()}')
