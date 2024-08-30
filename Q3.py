# 3) Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar

num = int(input("Informe um numero: "))

div = num % 2
if div == 0:
  print("PAR")
else:
  print("IMPAR")


