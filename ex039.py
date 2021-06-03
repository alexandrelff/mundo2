#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar no serviço militar
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
anoNasc = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade > 18:
    print('Você tem {} anos, deveria ter se alistado há {} anos.'.format(idade, idade - 18))
elif idade < 18:
    print('VocÊ tem {} anos, faltam {} anos para o seu alistamento.'.format(idade, 18 - idade))
else:
    print('Você tem {} anos. Precisa se alistar imediatamente!!!'.format(idade))
