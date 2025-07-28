arquivo_or = "us-counties.txt"
with open (arquivo_or, "r") as arquivo1:
    for linha in arquivo1.readlines():
        print(linha)