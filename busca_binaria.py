def busca_binaria(lista, alvo, inicio, fim):
    if inicio > fim: # se os índices se cruzarem
        return None # não achou o alvo, retorna None
    meio = (inicio + fim) // 2 # acha o meio da lista
    if lista[meio] == alvo:
        alvo_e_indice = {'alvo': lista[meio], 'indice': meio} # retorna o próprio alvo e o índice
        return alvo_e_indice # se achar o alvo no meio (primeira busca), o retorna
    if lista[meio] < alvo:
        return busca_binaria(lista, alvo, meio + 1, fim) # se o meio for menor que o alvo, chama a função de volta começando do índice sucessor ao meio
    return busca_binaria(lista, alvo, inicio, meio - 1) # se o meio for maior que o alvo, chama a função de volta terminando no índice antecessor ao meio

# cria a lista e define o alvo
minha_lista = [1, 3, 5, 7, 9, 11, 13]
meu_alvo = 11

# chama a função
resultado = busca_binaria(minha_lista, meu_alvo, 0, len(minha_lista) - 1)

if resultado is not None:
    print(f"Alvo encontrado: {resultado['alvo']} | Posição: arr[{resultado['indice']}]")
else:
    print("Alvo não encontrado.")

# =)!