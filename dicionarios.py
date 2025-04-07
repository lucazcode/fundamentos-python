print(">> Fundamentos em dicionários em Python")

# pular linha
space = "\n" + "-"*40 + "\n"

# dicionário vazio
dict_vazio = {}

# dicionário com dados iniciais
dict_preenchido = {'nome': 'Lucas', 'idade': 20}
print("Dicionário: ", dict_preenchido)

print(space)

# atribuindo dados às variáveis
nome = dict_preenchido['nome']
idade = dict_preenchido['idade']
print("Nome: ", nome, "\nIdade: ", idade)

print(space)

# se tentar acessar uma chave que não existe, um erro será gerado (KeyError).
# para evitar isso, use o método get.
profissao = dict_preenchido.get('profissao', 'Não especificado')
print("Profissão: ", profissao)

print(space)

# modificando um elemento existente
dict_preenchido['idade'] = 21

# adicionando um novo elemento
dict_preenchido['profissao'] = 'Estudante'
profissao = dict_preenchido['profissao']
print("Profissão: ", profissao)

print(space)

# removendo um elemento específico
idade = dict_preenchido.pop('idade')
print("Dicionário: ", dict_preenchido) # aqui, o dicionário não contém mais o dado
print("Idade: ", idade) # a variável ainda guarda o valor da idade até que seja alterada

print(space)

# colocando o dado de volta no dicionário
dict_preenchido['idade'] = idade
print("Dicionário: ", dict_preenchido)

print(space)

# removendo todo o dicionário (comentado)
# del dict_preenchido

# obtendo todas as chaves (sem os dados)
chaves = dict_preenchido.keys()
print("Chaves: ", chaves)

print(space)

# obtendo todos os dados
dados = dict_preenchido.values()
print("Dados: ", dados)

print(space)

# iteração em dicionários
for chave, dado in dict_preenchido.items():
    print(f"{chave}: {dado}")

# dicionários aninhados (um dentro do outro)
animais = {
    'gato': {'nome': 'Tom', 'idade': '7'},
    'cachorro': {'nome': 'Rex', 'idade': '10'}
}

print(space)

# acessando dados dentro de dicionários que estão dentro de outros dicionários)
nome_gato = animais['gato']['nome']
idade_gato = animais['gato']['idade']
print(f"Idade do gato {nome_gato}: {idade_gato} anos")

print(space)

# iteração em dicionários dentro de outros dicionários
for especie, dados in animais.items():
    nome = dados['nome']
    idade = dados['idade']
    print(f"Espécie: {especie} | Nome: {nome} | Idade: {idade}")

print(space)

# verificar condição no dicionário
if 'profissao' in dict_preenchido:
    print(f"{dict_preenchido['nome']} possui uma profissão.")
else:
    print(f"{dict_preenchido['nome']} não possui uma profissão.")

# =)!