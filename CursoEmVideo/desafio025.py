#Faça um programa que leia o nome de uma pessoa
#e veja se no nome dela tem 'SILVA'

name = str(input('Qual o seu nome completo? '))
name = name.upper()
print('Seu nome tem Silva? {}'.format('SILVA' in name))
