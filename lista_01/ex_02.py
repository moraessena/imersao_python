preco = float(input("informe o valor do produto: "))
desconto_percentual = float(input("informe o valor do desconto em percentual: "))

desconto_real = preco * (desconto_percentual / 100)
preco_final = preco - desconto_real
print(f"Valor com desconto: R${preco_final:.1f}")