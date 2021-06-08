#Faça um programa que leia um número qualquer e mostre o seu fatorial
# ex: 5! = 5x4x3x2x1 = 120
n1 = int(input('Cálculo de Fatorial\n'
              'Digite um número inteiro: '))
n2 = n1
fatorial = 1
print('{}! = '.format(n1), end='')
while n2 != 0:
    print('{}'.format(n2), end='')
    print(' x ' if n2 > 1 else ' = ', end='')
    fatorial *= n2
    n2 -= 1
print('{}'.format(fatorial))
