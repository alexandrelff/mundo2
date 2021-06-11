# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
won = 0
print('>' * 5, 'ÍMPAR OU PAR GAME', '<' * 5)
while True:
    pc = randint(0, 10)
    choice = ' '
    while choice not in 'pPiI':
        choice = str(input('Você quer Ímpar ou Par? [I/P] ')).strip()
    playerNum = int(input('Qual a sua jogada?'))
    sum = pc + playerNum
    result = 'ÍMPAR' if sum % 2 !=0 else 'PAR'
    print(f'Você jogou {playerNum} e o computador {pc}. O total foi {sum}\n'
          f'O RESULTADO FOI {result}')
    if result == 'PAR' and choice in 'pP':
        print('Você ganhou! Vamos jogar novamente...')
        print('=-' * 5)
        won += 1
    elif result == 'ÍMPAR' and choice in 'iI':
        print('Você ganhou! Vamos jogar novamente...')
        print('=-' * 5)
        won += 1
    else:
        print('Você perdeu!')
        print('=-' * 15)
        break
print('GAME OVER\n'
      f'Você venceu {winCount} vez(es).')
