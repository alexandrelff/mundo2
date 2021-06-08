#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# prograssão usando a estrutura while.
print('-=' * 3, 'PROGRESSÃO ARITMÉTICA', '=-' * 3)
pt = int(input('Digite o Primeiro Termo: '))
r = int(input('Digite a Razão da progressão: '))
print('Os 10 primeiros termos são:')
count = 1
while count != 10:
    print('{} ➜ '.format(pt), end='')
    pt += r
    count += 1
print(pt)
