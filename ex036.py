#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário então o empréstimo será negado.

print('==*=' * 3, ' Validação de Empréstimo ', '=*==' * 3)
valor = float(input('Digite o valor da casa: R$'))
renda = float(input('Digite a renda do comprador: R$'))
tempo = int(input('Digite o tempo, em anos, desejado para quitação do débito: '))

mensal = valor / (tempo * 12)

if (mensal > (renda * 0.3)):
    print('Desculpe! Empréstimo negado, o valor da prestação mensal (R${:.2f}) excede 30% da renda (R${:.2f}).'.format(mensal, renda * 0.3))
else:
    print('Parabéns! Empréstimo aprovado!')

