#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram
# no interalo de 1 até 500
soma = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        soma += i
print(soma)
