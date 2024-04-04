valor_produto = float(input("informe o valor do produto: "))
qtd_parcelas = int(input("informe o quantidade de parcelas: "))

valor_parcela = valor_produto / qtd_parcelas
print(f"Valor de cada parcela R$ {valor_parcela:.1f}")