idade = int(input("informe a sua idade: "))
if 0 <= idade <= 12:
    print("É criança")
elif 12 < idade <= 20:
    print("É adolescente")
elif 20 < idade <= 64:
    print("É adulto")
elif idade > 64:
    print("É idoso")
else:
    print("Idade inválida")