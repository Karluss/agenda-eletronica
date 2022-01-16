lista_nome = []

def inserir(lista):
    nome = input("Digite o nome que deseja adicionar à lista: ")
    lista.append(nome)
    print(lista)

def buscar(lista):
    nome = input("Digite o nome que deseja buscar: ")
    if nome in lista:
        print(nome, ",no índice ", lista.index(nome))
    else:
        print("Nome não encontrado")

def remover(lista):
    nome = input("Digite o nome que deseja deletar: ")
    if nome in lista:
        lista.remove(nome)
        print(lista)
    else:
        print("Nome não encontrado. Nenhum nome foi apagado.")

def crescente(lista):
    lista.sort()
    print("Lista em ordem crescente:")
    print(lista)

def decrescente(lista):
    lista.sort()
    lista.reverse()
    print("Lista em ordem decrescente:")
    print(lista)

def menu():
    print("\nBem-vindo à Agenda Eletrônica!")
    print("\n1. Inserir nome")
    print("2. Buscar nome")
    print("3. Remover nome")
    print("4. Colocar em ordem crescente")
    print("5. Colocar em ordem decrescente")
    print("6. Sair")
    print("\nInsira o número da opção que deseja:")
    opcao = int(input())
    while opcao < 1 or opcao > 6:
        print("\nOpção inválida, tente novamente.")
        print("Insira o número da opção que deseja:")
        opcao = int(input())
    return opcao

def main(): 
    opcao = menu()
    while opcao != 6:
        if opcao == 1:
            inserir(lista_nome)
            opcao = menu()

        elif opcao == 2:
            buscar(lista_nome)
            opcao = menu()

        elif opcao == 3:
            remover(lista_nome)
            opcao = menu()

        elif opcao == 4:
            crescente(lista_nome)
            opcao = menu()

        elif opcao == 5:
            decrescente(lista_nome)
            opcao = menu()

main()
