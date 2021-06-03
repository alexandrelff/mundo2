#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('Agora escolha uma das opções de conversão de base:\n'
      '1 - Converter para Binário\n'
      '2 - Converter para Octal\n'
      '3 - Converter para Hexadecimal')
opcao = int(input('Opção escolhida: '))
if opcao == 1:
    print('O número {} convertido para Binário é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print("O número {} convertido para Octal é igual a {}.".format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para Hexadecimal é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida.')