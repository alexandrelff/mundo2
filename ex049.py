#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número: '))
print('A tabuada do número {} é:'.format(n))
for i in range(0, 11):
    print('{} x {:2} = {}'.format(n, i, n * i))
