import base64
import funcoesb64
print("1. Codificar \n2. Decodificar \n3. Sair")
escolha = int(input("Escolha uma opção: "))
while escolha > 0 and escolha < 3:
    if escolha == 1:
        imagem = input("Digite o nome do arquivo de imagem (tem que estar nesta pasta): ")
        rec = input("Digite o nome do arquivo que receberá a base64: ")
        funcoesb64.codificacao(imagem, rec)
    elif escolha == 2:
        base64_file = input("Digite o nome do arquivo base64 (tem que estar nesta pasta): ")
        rec = input("Digite o nome do arquivo que receberá a imagem: ")
        funcoesb64.decodificacao(base64_file, rec)
    elif escolha == 3:
        print("Saindo do programa...")
        break
    escolha = int(input("Escolha uma opção: "))