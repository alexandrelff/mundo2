# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada vaçor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo
print('=' * 5, 'TABUADA', '=' * 5)
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        print('-' * 15)
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('-' * 15)
print('PROGRAMA ENCERRADO')
