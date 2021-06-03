#Crie um programa que leia uma frase qualquer e diga se é um palíndromo, desconsiderando os espaços.
#Ex.: apos a sopa/ a sacada da casa/ a torre da derrota...
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitade NÃO é um palíndromo!')