valor_inicial = float(input("informe o valor inicial: "))
taxa_juro = float(input("informe a taxa de juro: "))
tempo = int(input("informe o período em meses: "))

valor_futuro = valor_inicial + (valor_inicial * (taxa_juro /100) * tempo)
print(f"Valor futuro: {valor_futuro:.1f}")