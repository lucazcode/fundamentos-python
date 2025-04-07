# cria a lista e define o alvo
minha_lista = [1, 3, 5, 7, 9, 11, 13]
meu_alvo = 11

def hash_map(lst, alvo):
    dicionario = {valor: i for i, valor in enumerate(lst)} # cria um dicionário com o valor e o índice, respectiviamente, dos dados da lista
    if alvo not in dicionario:
        return None
    return {'alvo': alvo, 'indice': dicionario[alvo]} # retorna o alvo e o índice

resultado = hash_map(minha_lista, 11)
if resultado is None:
    print("Alvo não encontrado na lista.")
else:
    print(f"Alvo encontrado na lista: {resultado['alvo']} | Índice: arr[{resultado['indice']}]")

# =)!