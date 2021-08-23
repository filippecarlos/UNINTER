
lista = [] # Lista começa vazia
dicionario = { }

# Função para cadastrar produto via append
def cadastra_produto(produto_para_cadastrar: dict):
    lista.append(produto_para_cadastrar)
    return

# Menu para saber se quer cadastrar
opcao = int(input('Cadastrar produto? 0 - Não     1 - Sim '))
while opcao == 1:
    produto_novo = {} # PRoduto novo é uma variavel com dicionario vazio

    produto_novo['codigo'] = int(input('Digite o código do produto: '))

    #Validador se o cod não é zero
    if produto_novo['codigo'] == 0:
        print('Código 0, encerrando cadastro de produtos.')
        break # Sai desse laço de repetição

    # Inicia o imput
    produto_novo['estoque'] = int(input('Digite a quantidade em estoque: '))
    produto_novo['minimo'] = int(input('Digite a quantidade mínima do estoque: '))

    cadastra_produto(produto_novo)

    #Validador se quer caastrar mais produto
    opcao = int(input('Cadastrar produto? 0 - Não     1 - Sim '))

# Validador se a lista for >0 com retorno em tela com a tabela
if len(lista) > 0:
    print('Lista de produtos por código em ordem crescente:')
    print("Código".center(16), end='') # end faz com que se continue na msm linha
    print("Estoque".center(16), end='') # end faz com que se continue na msm linha
    print("Mínimo".center(16))

    # PAra cada prod nessa lista ja ordenada eu mostro na tela
    for produto in sorted(lista, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(16), end='')  # end faz com que se continue na msm linha
        print(str(produto['estoque']).center(16), end='')  # end faz com que se continue na msm linha
        print(str(produto['minimo']).center(16))
else:
    print('Que pena, você ainda nãocadastrou nenhum produto.')

