
# fazer um algoritmo que roda em looping infinito
usuarios = []
while True:
    print("="*30)
    print("Cadastro de usuários")
    print("="*30)
    print("1- Cadastrar usuário")
    print("2- Atualizar Usuário")
    print("3- Deletar Usuário")
    print("4- Listar Usuário")
    print("q - Sair")
    opcao = input("Digite sua opção:")
    
    if opcao == "1":
        nome = input("Digite seu nome:")
        usuarios.append(nome)

    elif opcao == "2":
        nome = input("nome que deseja atualizar")
        clientes = ["Jéssica","Gabriel"]

nome = input("Digite o nome da pessoa que deseja atualizar:")
indice = clientes.index(nome) 

print(indice)
novo_nome = input("Digite o novo nome que deseja atualizar:")
clientes[indice] = novo_nome

    elif opcao == "3":
        nome=input("Nome que deseja remover")
        usuarios.remove(nome)

    elif opcao == "4":
        print(usuarios)

    elif opcao == "q":
        break
    else:
        print("Resposta Inválida")