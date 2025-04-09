import os

# define um caminho absoluto:
# usuario = os.getlogin() # atribui o nome de usuário da máquina na variável automaticamente
# caminho_arquivo = f"C:/Users/{usuario}/Desktop/arquivo_texto.txt" # define o caminho na área de trabalho do usuário

# define um caminho relativo:
caminho_arquivo = "pasta_arquivo_texto/arquivo_texto.txt"

if os.path.exists(caminho_arquivo): # se o caminho do arquivo existe
    print(f"[O caminho '{caminho_arquivo}' existe]")

    if os.path.isfile(caminho_arquivo): # se o arquivo existe
        print("[É um arquivo]")
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: # abre o arquivo e se obter sucesso, fecha a leitura
            conteudo = arquivo.read()
            print(conteudo)
    elif os.path.isdir(caminho_arquivo): # se o arquivo for uma pasta
        print("É uma pasta")
else:
    print("O caminho não existe")

# =)!