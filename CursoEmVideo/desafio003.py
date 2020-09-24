'''
Ler dois números e dizer a soma entre eles
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))

#processamento
soma = n1+n2

#saida
#print('A soma entre', n1, 'e', n2, 'é igual a', soma)
print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
