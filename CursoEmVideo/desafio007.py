'''
Desenvolva um programa que leia as duas notas de um aluno, calcule, e mostre sua média.
'''
#Entrada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#Processamento
m = (n1 + n2) / 2

#Saída
print('A média entre {:.2f} e {:.2f} é {:.2f}'.format(n1, n2, m))
