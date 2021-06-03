#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
#- Abaixo de 18.5: Abaixo do peso
#- Entre 18.5 e 25: Peso ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade mórbida

print('=' * 5, ' CÁLCULO DO IMC ', '=' * 5)
print('Informações do paciente')
alt = float(input('Altura (m): '))
peso = float(input('Peso (kg): '))

imc = peso / (alt ** 2)

if imc < 18.5:
    print('IMC: {:.2f}\nClassificação: Abaixo do Peso.'.format(imc))
elif imc < 25:
    print('IMC: {:.2f}\nClassificação: Peso ideal.'.format(imc))
elif imc < 30:
    print('IMC: {:.2f}\nClassificação: Sobrepeso.'.format(imc))
elif imc < 40:
    print('IMC: {:.2f}\nClassificação: Obesidade.'.format(imc))
else:
    print('IMC: {:.2f}\nClassificação: Obesidade Mórbida.'.format(imc))
