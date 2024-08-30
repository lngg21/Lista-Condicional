# 4) Faça um algoritmo que leia dois valores inteiros A e B se os balores forem iguais deverá se somar os dois, caso o contrário mutiplique A por B.
# Ao final de qualquer um dos cálculos deve=se atribuir o resultado para uma variável C e mostrar seu contúdo na tela

A = int(input("Digite um numero: "))
B = int(input("Digite um outro numero: "))

Csoma = A + B

Cmult = A * B

if A == B:
  print ("C = " , Csoma)
else:
  print("C = " , Cmult)