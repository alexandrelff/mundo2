# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada (flag). No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando a flag)
soma = 0
contador = 0
while True:
    n = int(input('Digite um número inteiro [\'999\' para encerrar]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Você digitou {contador} números, o somatório deles é igual a {soma}.')

