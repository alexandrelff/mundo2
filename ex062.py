#Melhore o desafio 061, perguntando para o usuário se ele uer mostrar mais termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
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
resp = int(input('Quantos termos você quer mostrar a mais? '))
count = resp
while resp != 0:
    while count > 1:
        pt += r
        print('{} ➜ '.format(pt), end='')
        count -= 1
    print(pt + r)
    resp = int(input('Quantos termos você quer mostrar a mais? '))
print('Programa finalizado.')
