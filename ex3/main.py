laura = set(input("Lista de Laura:").lower().split(','))
ana = set(input("Lista de Ana:").lower().split(','))

comum = laura.intersection(ana)
exclusivo_laura = laura.difference(ana)
exclusivo_ana = ana.difference(laura)

print(f"o que tem em comum entre laura e ana é:{', '.join(comum)}")
print(f"exclusivo da laura é:{', '.join(exclusivo_laura)}")
print(f"exclusivo da Ana é:{', '.join(exclusivo_ana)}")
