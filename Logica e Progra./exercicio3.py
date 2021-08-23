
import random # Importação da biblioteca
#Variavel doadores inicia comuma lista vazia para ser gravada de acordo com  a sua doação
colaboradores = []
#Função de cadastro que recebe o valor da doação em float e nome str
def cadastra(nome:str, doacao:float):
    colaboradores.extend( ((nome + ' ') * int(doacao//10)).split() )
    return
#função que embaralha a lista de doadores retornando um dos valores
def sorteio():
    random.shuffle(colaboradores)
    print(f'Lista embaralhada: {colaboradores}')
    print(1 * '\n') # Quebra de linha para melhor vizualização dos resultados
    return random.choice(colaboradores)
# Valdador para saber se ainda quer continuar com o processo
opcao = int(input('Cadastrar doador? 0 - Não     1 - Sim '))
while opcao == 1:
    doador = input('Insira o nome do doador: ')
    valor = float(input('Insira o valor da doação: '))
    cadastra(doador, valor)
    # Valdador para saber se ainda quer continuar com o processo
    opcao = int(input('Cadastrar doador? 0 - Não     1 - Sim '))

# Dados aceitos a função cadastrar_doador se torna True incluindo novos doadores na lista mantendo os antigos
if len(colaboradores) > 0:
    print(f'Lista de doadores para sorteio: {colaboradores}')
    print(1 * '\n') #Quebra de linha para melhor vizualização dos resultados
    print(f'O vencedor(a) foi: {sorteio()}')
    print(1 * '\n') #Quebra de linha para melhor vizualização dos resultados
