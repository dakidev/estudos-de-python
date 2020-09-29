'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
'''

#Entrada
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

#Processamento
preço = (60 * dias) + (0.15 * km)

#Saída
print('O total a pagar é de R${}'.format(preço))
