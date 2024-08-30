# 1) Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C

A = input("Digite o valor de A:")
B = input("Digite o valor de B:")
C = input("Digite o valor de C:")


soma = A + B

if soma < C:
  print("CERTO")
else:
  print("ERRADO")
