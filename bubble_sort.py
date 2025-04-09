# cria a lista desordenada e a formata
lista_desordenada = [3,1,2,5,4]
print("Lista desordenada: ", lista_desordenada)

# função bubblesort
def bubble_sort(lst):
    n = len(lst) # define 'n' com o tamanho da lista
    for i in range(n-1): # itera sob todos o números da lista, até que todos estejam ordenados
        troca = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]: # se o número a ser comparado for maior que seu sucessor
                lst[j], lst[j+1] = lst[j+1], lst[j] # troca os números de posição
                troca = True # confirma que houve a troca
        if not troca: # se não houver troca na primeira iteração completa, o array está ordenado, quebre o loop
            break
    return lst

# chama a função e a formata o resultado
lista_ordenada = bubble_sort(lista_desordenada)
print("Lista ordenada: ", lista_ordenada)

# função inverter a lista
def invert_array(lst):
    n = len(lst) # define 'n' com o tamanho da lista
    i_lst = [] # cria uma lista vazia
    for i in range(n-1, -1, -1): # itera sob a lista de trás para frente
        i_lst.append(lst[i]) # define os valores da nova lista com os valores da lista original de trás para frente
    return i_lst

# chama a função e a formata o resultado
lista_invertida = invert_array(lista_ordenada)
print("Lista ordenada e invertida: ", lista_invertida)

# =)!