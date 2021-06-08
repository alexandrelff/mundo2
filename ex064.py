#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando a flag)

count = -1 #devido ao input da flag
soma = -999 #devido ao input da flag
n = 0
while n != 999:
    n = int(input('Digite um número inteiro (999 para encerrar): '))
    soma += n
    count += 1
print('Você digitou {} números, a soma entre eles é igual a {}.'.format(count, soma))
