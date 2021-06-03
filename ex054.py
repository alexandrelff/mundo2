#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas jão são maiores. Considerar 21 anos como maioridade.
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for i in range(0, 7):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i + 1)))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Nesse grupo tem {} pessoas maiores de 21 anos de idade, e {} menores de 21 anos'.format(maior, menor))