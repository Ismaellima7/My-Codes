n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto {} e a divisão {:.2f}. '.format(a, m, d), end= ' ')
print('A divisão inteira corresponde a {} e a potência {}. '.format(di, e))