#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
# e condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço normal
#- 3x ou mais no cartão: 20% de jutors
print('=*' * 4, 'PAGAMENTO', '*=' * 4)
valor = float(input('Valor do produto: R$'))
pag = int(input('Formas de pagamento:'
      '\n1 - À vista no dinheiro ou cheque'
      '\n2 - À vista no cartão de débito'
      '\n3 - Em 2x no cartão de crédito'
      '\n4 - Em 3x ou mais no cartão de crédito'
      '\nDigite a opção escolhida: '))
if pag == 1:
    print('O valor com desconto de 10% custará: R${:.2f}'.format(valor * 0.9))
elif pag == 2:
    print('O valor com desconto de 5% custará: R${:.2f}'.format(valor * 0.95))
elif pag == 3:
    print('O valor será o preço normal do produto. R${:.2f}'.format(valor))
elif pag == 4:
    print('O valor com juros de 20% custará R${:.2f}'.format(valor * 1.2))
else:
    print('A opção digitada não corresponde às informadas. Tente novamente.')
