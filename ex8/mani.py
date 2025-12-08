participantes = {

    "Mariana": 25,

    "Carlos": 32,

    "Beatriz": 28,

    "Rafael": 35

}

print(f'Nomes dos partivipantes:{', '.join(participantes.keys())}')
print(
    # nessse caso é necessario o uso de str pois join serve apenas para string e não numericos
    f'Idades dos partivipantes:{', '.join(str(idade) for idade in participantes.values())}')
print('Participantes e suas idades:')
for nome, idade in participantes.items():
    print(f'{nome}:{idade}anos')
