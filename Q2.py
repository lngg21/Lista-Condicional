# 2) Faça um algoritmo que leia o nome, sexo e o estado civil de uma pessoa. Caso sexo seja "F" e estado civil seja "CASADA", solicitar o tempo de casada(anos)
sexo = input("Digite o seu sexo(F/M):")
nome = input("Digite o seu Nome:")
ec = input("Digite o seu estado civil(C/S):")

if sexo == "F" and ec == "C":
  tc = input("Quanto tempo de casado: ")
else:
  print("Obrigado")

print( nome + " " + sexo + " " + ec + " " + tc)