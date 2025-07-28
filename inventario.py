inventario = {}
print("Adicionando um inventário")
op = int(input("Digite:\n1 - Registrar ativo \n2 - Persistir em arquivo .csv \n3 - Exibir os ativos armazenados \n4 - Sair"))
print("Indicamos fazer os passos em sequência")
while op > 0 and op < 5:
    if op == 1:
        continuar = "S"
        while continuar == "S":
            inventario[input("Digite o número patrimonial: ")] = [input("Descrição do produto"),
                                                                  input("Data da atualização: "),
                                                                  input("Nome do departamento: ")]
            continuar = input("Digite <s> para continuar").upper()
            if continuar == "n" or continuar == "N":
                print("Saindo")
    elif op == 2:
        with open("inventario.csv", "a") as arquivo_csv:
            for chave, valor in inventario.items():
                arquivo_csv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2]+"\n")
                print("Está no arquivo .csv agora!!!")
    elif op == 3:
        with open("inventario.csv", "r") as arquivo_csv:
            for linha in arquivo_csv.readlines():
                print(linha)
    elif op == 4:
        print("...Saindo....")
        break
    op = int(input("Digite:\n1 - Registrar ativo\n2 - Persistir em arquivo .csv \n3 - Exibir os ativos armazenados \n4 - Sair"))
    