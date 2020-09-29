'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
'''

#Entrada
salar = float(input('Qual o salário do funcionário? R$'))

#Processamento
porcen = (salar * 15) / 100
aument = salar + porcen

#Saída
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salar, aument))
