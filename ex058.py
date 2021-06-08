#Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agorao jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint
from time import sleep
print('O computador está sorteando um número entre 0 e 10')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
pcNum = randint(0, 10)
num = int(input('Tente acertar o número sorteado, qual o seu palpite: '))
count = 1
while num is not pcNum:
    num = int(input('Aaah, infelizmente não acertou. Tente novamente: '))
    count += 1
print('Parabéns, você acertou!\n'
      'O número sorteado foi {}!\n'
      'Você conseguiu na {}ª tentativa.'.format(pcNum, count))
