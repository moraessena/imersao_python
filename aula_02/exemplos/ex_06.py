sexo = input("informe seu sexo 'F' ou 'M': ")
idade = int(input("informe a sua idade: "))
if sexo == 'M' and idade>=18:
    print(f"É necessário emitir a carteira de reservista.")
else:
    print(f"Não é necessário emitir a carteira de reservista")