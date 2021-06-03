#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('Digite o peso em kg da {}ª pessooa: '.format(i + 1)))
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso foi {}kg, e o menor foi {}kg'.format(maior, menor))
