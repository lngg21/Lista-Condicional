# 7) Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar,
# imprimir o resultado desta operação.

num = int(input("Digite um numero: "))

div = num%2

cin = num + 5
oit = num + 8

if div == 0:
  print("Nuumero pós soma:" , cin)
else:
  print("Numero pós soma:", oit)