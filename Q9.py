# 9) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# ● para homens: (72.7 * h) – 58;
# ● para mulheres: (62.1 * h) – 44.7.

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo:(F/M) ").upper()

if sexo == "F":
  pif = (62.1 * altura) - 44.7
  print("O seu peso ideal é: {:.2f}".format(pif))

elif sexo == "M":
  pim = (72.7 * altura) - 58
  print("O seu peso ideal é: {:.2f}".format(pim))

else:
  print("Digite o sexo por F(feminino) ou M(masculino)")


