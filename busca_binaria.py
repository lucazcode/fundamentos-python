# com recursividade
def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio > fim: # se os índices se cruzarem
        return None # não achou o alvo, retorna None
    meio = (inicio + fim) // 2 # acha o meio da lista
    if lista[meio] == alvo:
        alvo_e_indice = {'alvo': lista[meio], 'indice': meio} # retorna o próprio alvo e o índice
        return alvo_e_indice # se achar o alvo no meio (primeira busca), o retorna
    if lista[meio] < alvo:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim) # se o meio for menor que o alvo, chama a função de volta começando do índice sucessor ao meio
    return busca_binaria_recursiva(lista, alvo, inicio, meio - 1) # se o meio for maior que o alvo, chama a função de volta terminando no índice antecessor ao meio

# sem recursividade
def busca_binaria_iterativa(lista, alvo):
    esq, dir = 0, len(lista) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if alvo < lista[meio]:
            dir = meio - 1
        elif alvo > lista[meio]:
            esq = meio + 1
        else:
            alvo_e_indice = {'alvo': lista[meio], 'indice': meio}  # retorna o próprio alvo e o índice
            return alvo_e_indice
    return None


# cria a lista e define o alvo
minha_lista = [1, 3, 5, 7, 9, 11, 13]
meu_alvo = 11

# chama a função recursiva
resultado_recursivo = busca_binaria_recursiva(minha_lista, meu_alvo, 0, len(minha_lista) - 1)

if resultado_recursivo is not None:
    print(f"Alvo encontrado: {resultado_recursivo['alvo']} | Posição: arr[{resultado_recursivo['indice']}]")
else:
    print("Alvo não encontrado.")

# chama a função linear
resultado_iterativo = busca_binaria_iterativa(minha_lista, meu_alvo)

if resultado_iterativo is not None:
    print(f"Alvo encontrado: {resultado_iterativo['alvo']} | Posição: arr[{resultado_iterativo['indice']}]")
else:
    print("Alvo não encontrado.")

# =)!