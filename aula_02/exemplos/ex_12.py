mesada = float(input("Quanto você ganhou de mesada? "))
if mesada >= 50:
    print(f"Com R$ {mesada} é possível ir ao cinema!")
elif 50 > mesada >= 10:
    print("Peça mais dinheiro a sua mãe Kiko")
else:
    print("O que faço com menos de R$ 10,00")