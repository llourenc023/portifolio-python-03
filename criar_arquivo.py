# with open abre o arquivo
# opções:
    # r -> lê o arquivo
    # w -> modifica o arquivo
    # x -> arquivo no modo exclusivo
    # a -> adiciona o conteúdo ao final do arquivo
    # t -> retorna o conteúdo do arquivo como uma string. Usa-se com o r antes, portanto rt
# é recomendado colocar o caminho do arquivo como uma variável:
arquivo = "us-counties.txt"
with open(arquivo, "w") as arquivo1:
    arquivo1.write("Hello world!")
    arquivo1.write("\nSantos Futebol clube")
    print("Sucesso!")