# 12) Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas
# 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de
# aproveitamento, usando a fórmula:
# MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7
# A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno,
# suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a
# mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.
# Média de aproveitamento Conceito
# >= 90 A
# >= 75 e < 90 B
# >= 60 e < 75 C
# >= 40 e < 60 D
# < 40 E

n1 = float(input("Qual foi sua primeira nota: "))
n2 = float(input("Qual foi sua segunda nota: "))
n3 = float(input("Qual foi sua terceira nota: "))

me = (n1+n2+n3)/3

ma = (n1+n2 * 2 + n3 * 3 + me)/7

nome = input("Digite seu nome: ")
numero = int(input("Digite seu numero: "))


def calc_conceito():
  if ma >= 9.0:
    print("Aprovado! Conceito: A ")
  elif ma>= 7.5 and ma< 9.0:
    print("Aprovado! Conceito: B")
  elif ma>=6.0 and ma<7.5:
    print("Aprovado! Conceito: C")
  elif ma >= 4.0 and ma < 6.0:
    print("Reprovado! Conceito: D")
  else: # ma < 40
    print("Reprovado! Conceito: E")

calc_conceito()

def exibirInfo():
  print("Numero: ", numero)
  print("Nome: ", nome)
  print(f"Média: {me:.2f}")
  print(f"MA: {ma:.2f}")
  calc_conceito()

exibirInfo()
