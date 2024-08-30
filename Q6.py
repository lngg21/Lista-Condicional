# 6) Escreva um algoritmo que lê dois valores booleanos(lógicos) e então determina
# se amboms são VERDADEIROS ou FALSOS.

A = input("Digite V/F:").upper()
B = input("Digite F/V").upper()


if A == 'V' and B == 'V':
  print("Ambos são verdadeiros")

elif A == 'V' and B == 'F': # Changed V to 'V' and F to 'F'
  print("Apenas A é verdadeiro")

elif A == 'F' and B == 'V': # Changed F to 'F' and V to 'V'
  print("Apenas B é verdadeiro")

else:
 print("Ambos são falsos")