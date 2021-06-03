#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima: MASTER
from datetime import date
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade <= 9:
    print('O atleta tem {} anos\nCategoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos\nCategoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos\nCategoria JÚNIOR.'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos\nCategoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos\nCategoria MASTER.'.format(idade))



