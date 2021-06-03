#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n = int(input('Digite um número inteiro: '))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if count == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo, ele foi divisível por {} números distintos.'.format(n, count))
