lista = [34,765,3,41,57,213,21,111,321,68]

# solução com for loop:
# pares = []
# for num in lista:
#     if num % 2 == 0:
#         pares.append(num)
#
# print("Números pares da lista: ", pares)

# solução com list comprehension:
# estrutura: valor para valor na lista se (condição)
pares = [num for num in lista if num % 2 == 0]
print("Números pares da lista: ", pares)

# list comprehension + tuplas:
# estrutura: valor, (string se condição, senão outra condição) para valor na lista
par_impar = [(num, "par" if num % 2 == 0 else "ímpar") for num in lista]
print("Classificação par/ímpar:", par_impar)

# =)!