from funcoes_inventario import *
inventario = {}
print("Programa inventário")

opcao = menu()
while opcao > 0 and opcao < 6:
    if opcao == 1:
        adicionar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        exibir = exibicao(inventario)
        for linha in exibir:
            lista = linha.split(";")
            print(f"Descrição: {lista[1]}") 
            print(f"Data: {lista[2]}")
            print(f"Departamento: {lista[3]}")
    elif opcao == 4:
        with open("inventario.csv", "w") as arquivo:
            arquivo.write(" ")  # Corrigido: passar inventario como argumento
            print("Ativo excluído com sucesso!")
    elif opcao == 5:
        print("Saindo do programa...")
        break
    opcao = menu()