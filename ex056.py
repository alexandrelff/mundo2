#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#- A média de idade do grupo.
#- Qual é o nome do homem mais velho.
#- Quantas mulheres têm menos de 20 anos.
soma = 0
somaM = 0
idadeM = 0
for i in range(0, 4):
    print('=' * 5, '{}ª PESSOA'.format(i + 1), '=' * 5)
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite F para feminino e M para masculino: ')
    soma += idade
    if sexo.lower() == 'm':
        if idade > idadeM:
            nomeM = nome
            idadeM = idade
    if sexo.lower() == 'f':
        if idade < 20:
            somaM += 1
print('A média de idade do grupo é {:.2f}.\n'
      'O homem mais velhor é {}, ele tem {} anos\n'
      'O grupo tem {} mulheres com menos de 20 anos.'.format(soma / 4, nomeM, idadeM, somaM))

