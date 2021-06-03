#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
opcoes = ('pedra', 'papel', 'tesoura')
print('=-' * 5, 'JOKENPÔ', '-=' * 5)
print('Escolha sua jogada\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
jogada = int(input('Qual a sua jogada: '))

pc = randint(0, 2)
print('O Computador jogou {}'.format(opcoes[pc]))

if jogada == 1:
    if pc == 0:
        print('Resultado: deu empate!')
    elif pc == 1:
        print('Resultado: o Computador ganhou!')
    else:
        print('Resultado: Parabéns! Você ganhou!')
if jogada == 2:
    if pc == 0:
        print('Resultado: Parabéns! Você ganhou!')
    elif pc == 1:
        print('Resultado: deu empate!')
    else:
        print('Resultado: o Computador ganhou!')
if jogada == 3:
    if pc == 0:
        print('Resultado: o Computador ganhou!')
    elif pc == 1:
        print('Resultado: Parabéns! Você ganhou!')
    else:
        print('Resultado: deu empate!')
