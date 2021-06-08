#Crie um programa que leia dois valores e mostre um menu na tela.
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
op = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while op != 5:
    print('===Menu de Operações===\n'
          '[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Números\n[ 5 ] Sair do programa')
    op = int(input('Digite a sua escolha: '))
    if op == 1:
        print('A some entre {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('O número {} é maior que {}.'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que {}.'.format(n2, n1))
        else:
            print('Ambos são {}, e portanto iguais.'.format(n1))
    elif op == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('O programa será encerrado.')
    else:
        print('Opção inválida, tente novamente.')
    sleep(3)
print('Programa finalizado.')
