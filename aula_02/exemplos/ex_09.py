nome = input("informe seu nome: ")
idade = int(input("informe sua idade: "))

if 9 <= idade <= 14:
    print(f"{nome} por favor dirija-se ao posto de saúde mais próximo para tomar a vacina de HPV")
else:
    print(f"{nome} não é ncessário tomar a vacina de HPV")