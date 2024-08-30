# 8) Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
# decrescente.

A = int(input("Digite um numero: "))
B = int(input("Digite outro numero: "))
C = int(input("Digite mais um numero: "))

if A != B != C != A:
  nums = [A, B, C]

nums.sort(reverse = True)
print("Valores em ordem decrescente:", nums)
else:
 print("Os valores devem ser diferentes entre si.")