texto1 = set(input("Digite um texto:").lower().split())
texto2 = set(input("Digite outro texto:").lower().split())

palavras_em_comum = texto1.intersection(texto2)

print(f'Palavras em comum:{palavras_em_comum}')
