valor_produto = float(input("informe o valor do produto: "))
taxa_imposto = float(input("informe a taxa de imposto: "))

valor_imposto = valor_produto * (taxa_imposto / 100)
valor_final = valor_produto + valor_imposto
print(f"Valor Final com Imposto: R$ {valor_final:.1f}")