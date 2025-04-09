# exception = evento que interrompe o fluxo de um programa
# exemplo: (ZeroDivisionError, TypeError, ValueError)
# tipos de controle: 1. try, 2. except, 3. finally

# ZeroDivisionError: exceção para operação que divide por 0
# exemplo de erro:
# num = int(input("Insira um número: "))
# print(num/0)

# TypeError: exceção para operação com valores de dados incorretos
# exemplo de erro:
# print(2 + "2")

# ValueError: exceção para definição de variáveis com tipos de dados incorretos
# exemplo de erro:
# nome = int("Nome")
# print(nome)

# exemplo de uso:

# tente isso
try:
    num = float(input("Insira um número para dividir 100: "))
    res = 100/num

# exceto isso
except ZeroDivisionError: # se a exceção de divisão por 0 for chamada
    print("[ERRO: Não é possível dividir por 0.]") # mostra mensagem e não interrompe o programa
except ValueError:
    print("[ERRO: Insira um número válido.]")
except Exception: # cobre qualquer exceção remanescente
    print("[ERRO: Algo deu errado.]") # prática não recomendada, não especifica erros

else: # se não houver nenhuma exceção, faça isso
    if res < 0.01:
        print(f"[Resultado: {res}]") # apresenta sem formatação de casas decimais
    else:
        print(f"[Resultado: {res:.2f}]") # apresenta com formatação até duas casas decimais

# independente de apresentar ou não exceções, finalmente faça isso
finally: # executa operações após a checagem de exceções
    print("[Fim do programa!]")

# =)!