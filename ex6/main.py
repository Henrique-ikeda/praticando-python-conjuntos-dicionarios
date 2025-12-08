item = {}

for x in range(3):
    nome = input("Digite o nome do produto:").lower()
    valor = input("Digite a quantidade:")
    item[nome] = valor

print(f'Dicionário de produtos:{item}')
