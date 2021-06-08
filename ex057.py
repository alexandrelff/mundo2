# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = str(input('Digite o seu sexo (M/F): ')).strip()
while sexo not in 'fmFM':
    sexo = str(input('Valor inválido, tente novamente.\n'
                     'Digite seu sexo novamente: (M/F) ')).strip()
if sexo in 'Ff':
    print('Sexo Feminino informado.')
else:
    print('Sexo masculino informado.')
