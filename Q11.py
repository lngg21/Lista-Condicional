# 11) Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal deetiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento

# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

def valor_final(preco, cod_pag):
  if cod_pag == 1:
    desconto = preco * 0.1
    valor_final = preco - desconto
  elif cod_pag == 2:
    desconto = preco * 0.15
    valor_final = preco - desconto
  elif cod_pag == 3:
    valor_final = preco
  elif cod_pag == 4:
    acrescimo = preco * 0.1
    valor_final = preco + acrescimo

  else:
        # Código inválido
        return "Código de pagamento inválido"

valor_final()


preco = float(input("digite o valor de etiqueta: "))
cod_pag = int(input("Digite um numero valido de 1 a 4: "))

resultado = valor_final(preco, cod_pag)

if isinstance(resultado, str):
    print(resultado)
else:
    print(f"O valor a ser pago é: R$ {resultado:.2f}")
