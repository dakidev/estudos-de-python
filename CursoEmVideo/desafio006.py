'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e raiz quadrada.
'''
#Entrada
n1 = int(input('Digite um número: '))

#Processamento/Saída
print('O dobro de {} vale {}'.format(n1, (n1*2)))
print('O triplo de {} vale {}'.format(n1, (n1*3)))
print('A raiz quadrada de {} vale {:.2f}'.format(n1, (n1**(1/2))))
