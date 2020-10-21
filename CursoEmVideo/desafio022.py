'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas
* O nome com todas as letras minúsculas
* Quantas letras ao todo (sem considerar espaços)
* Quantas letras tem o primeiro nome
'''

nome = str(input('Digite seu nome completo: '))
print('O nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Número de letras (sem considerar espaços): {}'.format(len(''.join(nome.split()))))

