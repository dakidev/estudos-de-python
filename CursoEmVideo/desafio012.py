'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
'''

#Entrada
preço = float(input('Digite o preço do produto: R$'))

#Processamento
v_desc = (preço * 5) / 100
desc = preço - v_desc

#Saída
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, desc))
