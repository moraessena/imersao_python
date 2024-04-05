especie = input("digite a espécie do animal: ")
if not especie.lower() == "cachorro" or not especie.lower() == "gato":
    print("O animal é doméstico.")
else:
    print("Espécie desconhecida pelo sistema.")