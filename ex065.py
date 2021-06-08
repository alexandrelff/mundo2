# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

n = int(input('Digite um valor: '))
maior = menor = soma = n
count = 1
resp = ''
while resp != 'N':
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()
    if resp == 'S':
        n = int(input('Digite um valor: '))
        soma += n
        count += 1
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / count
print('Você digitou {} valores.\n'
      'A média entre eles é igual a {}.\n'
      'O maior valor digitado foi {}, e o menor valor foi {}.'.format(count, media, maior, menor))

