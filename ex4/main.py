
permissoes_principais = set(input("Permissões principais: ").strip().lower().split(',')) 

permissoes_solicitadas = set(input("Permissões solicitadas: ").strip().lower().split(',')) 

verificador_de_permissoes = permissoes_solicitadas.issubset(permissoes_principais) 

if verificador_de_permissoes == True:
    print('As permissões solicitadas fazem parte das permissões principais.')

else:
    print('As permissões solicitadas não fazem parte das permissões principais.')