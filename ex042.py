#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais
#- Isósceles: dois lados iguais
#- Escaleno: todos os lados diferentes

r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('As retas formam um triângulo!!')
    if r1 == r2 == r3:
        print('O triângulo formado é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é ESCALENO')
    else:
        print('O triângulo formado é ISÓSCELES')
else:
    print('As retas não formam um triângulo.')