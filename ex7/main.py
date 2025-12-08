
estoque = {

    "Caderno universitário": 50,

    "Caneta azul": 120,

    "Borracha branca": 30

}


item = input("Nome do produto a ser atualizado:")
quantidade = input("Nova quantidade:")

if item in estoque:   # nesse caso é necessaio o if para confiramar se o item existe e se existir vai utilizar ele e não criar outro
    estoque[item] = quantidade
    print("Quantidade atualizada com sucesso!!")
    print(estoque)
else:
    print("Produto não encontrado no estoque.")
