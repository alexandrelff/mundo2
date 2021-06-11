# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será
# o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs.: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
print('=' * 30)
print(f'{"BANCO DEV":^30}')
print('=' * 30)
saque = int(input('Quanto você deseja sacar? R$ '))
valor = saque
ced = 50
totalCed = 0
while True:
    if valor >= ced:
        valor -= ced
        totalCed += 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} {"cédulas" if totalCed > 1 else "cédula"} de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalCed = 0
        if valor == 0:
            break
print('=' * 30)
print('Operação encerrada, O Banco Dev agradece. Volte sempre!')
