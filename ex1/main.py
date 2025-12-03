conjunto_convidados = set()

while True:
    nome = input("Digite o nome do convidado:")
    if nome.lower() == "sair":
        break
    conjunto_convidados.add(nome)

print(f"Convidados confirmados:{', '.join(conjunto_convidados)}")
