def menu():
    print("\nMenu:")
    print("1 - Adicionar item")
    print("2 - Salvar/Persistir inventário")
    print("3 - Exibir inventário")
    print("4 - Apagar inventário")
    print("5 - Sair")
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        return 0


def excluir(dicionario):
    with open("inventario.csv", "w") as arquivo:
        arquivo.write(" ")

def adicionar(dicionario):
    continuar = "S"
    while continuar == "S":
        dicionario[input("Adicione o número patrimonial de 4 dígitos: ")] = [input("Adicione uma descrição do produto: "),
                                                          input("Adicione a data de atualização: "),
                                                          input("Adicione o departamento do ativo: ")]
        continuar = input("Digite <S> para continuar e <N> para sair: ").upper()
        if continuar == "n" or continuar == "N":
            print("... Saindo ...")


def persistir(dicionario):
    with open("inventario.csv", "a") as arquivo:  # modo append para não apagar os antigos
        for chave, valor in dicionario.items():
            arquivo.write(chave + ";" + str(valor) + "\n")
    return "Dados adicionados ao arquivo"


def exibicao(dicionario):
    with open("inventario.csv", "r") as arquivo:
        linha = arquivo.readlines()
    return linha

def saida():
    return "...Saindo..."