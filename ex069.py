# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
count = plus18 = womenUnder20 = men = 0
while True:
    count += 1
    sex = ' '
    aws = ' '
    age = int(input(f'Digite a idade da {count}ª pessoa: '))
    while sex not in 'fFmM':
        sex = str(input('Digite o sexo: [F/M] ')).strip()[0]
    while aws not in 'sSnN':
        resp = str(input('Deseja continuar? [S/N]')).strip()
    if age > 18:
        plus18 += 1
    if sex in 'mM':
        men += 1
    if sex in 'fF' and age < 20:
        womenUnder20 += 1
    if aws in 'nN':
        break
print(f'Você cadastrou {count}.\n'
      f'Sendo {plus18} pessoas maiores de 18 anos.\n'
      f'Foram {men} homens cadastrados ao todo.\n'
      f'E {womenUnder20} mulheres com menos de 20 anos.')
