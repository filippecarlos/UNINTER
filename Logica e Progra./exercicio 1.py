

#Menu de seleção para saber se o usuario quer iniciar o programa ou não
comecar = int(input('Deseja inserir dados? 0 - Não     1 - Sim '))

# Laço de repetição para verificar se inicia ou encerra
while comecar == 1:
    aluno = input("Digite nome do aluno: ")
    nota = float(input("Digite a nota final do aluno de 0 - 10: "))

    # Inicio da verificação de nota e atribuição do conceito
    if 0 <= nota < 3:
        conceito = 'E'
    elif 3 <= nota < 5:
        conceito = 'D'
    elif 5 <= nota < 7:
        conceito = 'C'
    elif 7 <= nota < 9:
        conceito = 'B'
    elif 9 <= nota <= 10:
        conceito = 'A'
    else:# Essa 1°condição se a nota for maior que 10 - Minha condição para que o programa se encerre
      print('Nota inválida, encerrando o programa.')
      exit() # Sair do laço de repetição
    # Resultado final de acordo com a nota do aluno e seu conceito
    print(f"O aluno {aluno} tirou a nota {nota} e se enquadra no conceito {conceito}")
    comecar = int(input('Inserir dados? 0 - Não     1 - Sim '))
else: # Essa 2°condição só é valida se no inicio o usuario - Minha condição para que o programa se encerre
  print ("Obrigado por usar nosso programa")






