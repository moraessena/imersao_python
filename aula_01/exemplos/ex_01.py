ANO_ATUAL = 2024

nome = input("digite o nome: ")
ano_nascimento = int(input("digite o ano de nascimento: ")) 
tamanho = float(input("digite o tamanho: "))
sexo = input("digite seu sexo: ") 
matriculada = bool(input("informe se está matriculada: "))

matriculada = "sim" if matriculada else "não"

print("nome: ", type(nome))
print("idade: ", type(ano_nascimento))
print("tamanho: ", type(tamanho))
print("sexo: ", type(sexo))
print("matriculada: ", type(matriculada))

# to print a single { use {{

print(f"Olá {{{nome}}}, você tem {ANO_ATUAL - ano_nascimento} anos, mede {tamanho:.2f}, é do sexo {sexo} e está matriculada {matriculada}")