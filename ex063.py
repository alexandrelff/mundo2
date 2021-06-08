# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma sequência de Fibonacci.
#Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('==*== Sequência de Finonacci ==*==')
n = int(input('Quantos termos você deseja mostrar: '))
f1 = 0
f2 = 1
print('{} ➜ {}'.format(f1, f2), end='')
n -= 2
while n != 0:
    f3 = f1 + f2
    print(' ➜ {}'.format(f3), end='')
    n -= 1
    f1 = f2
    f2 = f3
print('\nPrograma finalizado.')

