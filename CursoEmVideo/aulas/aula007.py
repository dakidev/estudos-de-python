n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print(f'A soma entre o primeiro valor é: {s}')
print(f'A multiplicação entre os dois valores é: {m}')
print('A divisão entre os dois valores é: {:.3f}'.format(d))
print(f'A divisão inteira entre os dois valores é: {di}')
print(f'O primeiro valor elevado ao segundo é: {e}')
