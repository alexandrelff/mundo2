#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
#No final, mostre os 10 primeiros termos dessa progressão.
print('-=' * 3, 'PROGRESSÃO ARITMÉTICA', '=-' * 3)
pt = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão da progressão: '))
print('Os 10 primeiros termos são:')
for i in range(0, 10):
    print('{}'.format(pt), end=' -> ')
    pt += r
print('FIM')
