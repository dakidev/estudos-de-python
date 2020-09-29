'''
Crie um programa que leia quanto dinheiro a pessoa tem na carteira, e o converta em dólares
'''

#Entrada
real = float(input('Quanto dinheiro você tem na carteira? R$'))

#Processamento
#R$5,66 = US$1,00
dolar = real / 5.66

#Saída
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))
