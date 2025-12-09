vendas = {

    "Eletrônicos": [

        {"produto": "Smartphone", "quantidade": 5, "valor_unitario": 2000},

        {"produto": "Tablet", "quantidade": 3, "valor_unitario": 1500}

    ],

    "Eletrodomésticos": [

        {"produto": "Geladeira", "quantidade": 2, "valor_unitario": 3000},

        {"produto": "Micro-ondas", "quantidade": 4, "valor_unitario": 800}

    ],

    "Livros": [

        {"produto": "Livro A", "quantidade": 10, "valor_unitario": 50},

        {"produto": "Livro B", "quantidade": 5, "valor_unitario": 100}

    ]

}
valores_categoria = {}

for categoria, produtos in vendas.items():
    valor = 0
    for produto in produtos:
        valor += produto["quantidade"]*produto["valor_unitario"]
    valores_categoria[categoria] = valor


for categoria, valor in valores_categoria.items():
    print(f'{categoria}:{valor}')
