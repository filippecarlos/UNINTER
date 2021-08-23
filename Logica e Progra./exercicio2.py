# meu RU 749385
# Função para gerar e-mail com strings formatadas
def geracao_email(nome:str, sobrenome:str, ru: str):
    # Validação por if para não aceitar strings vazia
    if len(nome) > 0 and len(sobrenome) > 0:
        return 'Sr. ' + nome + ' ' + sobrenome + ', seu e-mail é ' + nome[0].lower() + sobrenome.lower() + ru + '@algoritmos.com.br' # Lower serve para alterar o tamanho da primeira letra para minusculo
    else:
        return None

#Input para receber o nome e sobrenome do usuário:
primeiro_nome = input('Digite o primeiro nome:')
ultimo_sobrenome = input('Digite o último sobrenome:')
ru = "85" # Meu RU
print(1 * '\n') #Quebra de linha para melhor vizualização dos resultados
print(geracao_email(primeiro_nome, ultimo_sobrenome, ru))
print(1 * '\n') #Quebra de linha para melhor vizualização dos resultados

