# 10) O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar
# umaindicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC = peso / ( altura )2

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo
# com a tabela abaixo.

# IMC em adultos Condição
# Abaixo de 18,5 Abaixo do peso
# Entre 18,5 e 25 Peso normal
# Entre 25 e 30 Acima do peso
# Acima de 30 obeso

peso = float(input("Insira o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso/(altura)**2


# Classifica a condição de acordo com o IMC
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Acima do peso")
else:  # IMC >= 30
    print("Obeso")
