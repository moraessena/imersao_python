valor_total_vendas = float(input("informe o valor total das vendas: "))
porcentagem_comissao = float(input("informe o percentual da comissão: "))

valor_a_receber = valor_total_vendas * (porcentagem_comissao / 100)
print(f"Valor da Comissão: R$ {valor_a_receber:.1f}")