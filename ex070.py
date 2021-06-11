# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total de gasto na compra.
# B) Quantos produtos custam mais de R$ 1000.
# C) Qual é o nome do produto mais barato.
sum = plus1000 = lowestPrice = count = 0
cheaperProduct = ''
while True:
    count += 1
    product = str(input('Nome do produto: '))
    price = float(input('Valor: R$'))
    sum += price
    if count == 1 or price < lowestPrice:
        cheaperProduct = product
        lowestPrice = price
    if price > 1000:
        plus1000 += 1
    aws = ' '
    while aws not in 'sSnN':
        aws = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if aws in 'nN':
        print('=' * 15)
        break
print(f'O somatório total foi R$ {sum:.2f}.\n'
      f'Foram cadastrados {plus1000} produtos acima de R$ 1000.\n'
      f'O produto mais barato foi {cheaperProduct}, custando R$ {lowestPrice:.2f}')



