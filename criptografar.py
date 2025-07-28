from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from funcoes_aes import *
from funcoes_des import *
escolha = menu_principal()
while escolha > 0 and escolha < 5:
    if escolha == 1:
        # Informa que está criando uma chave AES
        print("...Criando uma chave AES...")
        # Chama a função para criar uma chave AES
        chaves = criar_chave()
        # Abre (ou cria) o arquivo 'chave.bin' para escrita binária e salva a chave nele
        with open("chave.bin", "wb") as arquivo:
            arquivo.write(chaves)
        # Solicita ao usuário que digite o texto a ser criptografado e converte para bytes
        texto = input("Digite o texto: ").encode()
        # Informa que vai criptografar o texto
        print("...Criptografando o texto...")
        # Abre (ou cria) o arquivo 'Palavra.txt' para escrita binária e salva o texto criptografado
        with open("Palavra.txt", "wb") as arquivo:
            arquivo.write(criptografar(chaves, texto))
        # Informa que o texto foi criptografado
        print("...Texto criptografado...")
    elif escolha == 2:
        # Informa que vai exibir a chave AES
        print("...Exibindo chave AES...")
        # Abre o arquivo 'chave.bin' para leitura binária e lê a chave
        with open("chave.bin", "rb") as arquivo:
            chave_lida = arquivo.read()
            # Exibe a chave lida em formato hexadecimal
            print(f"Chave lida: {chave_lida.hex()}")
    elif escolha == 3:
        # Informa que vai descriptografar o texto
        print("...Descriptografando o texto...")
        # Abre o arquivo 'Palavra.txt' para leitura binária e lê o texto cifrado
        with open("Palavra.txt", "rb") as arquivo:
          texto_cifrado = arquivo.read()
        # Solicita ao usuário que digite a chave em hexadecimal para descriptografar
        chaves = input("Digite a chave para descriptografar: ")
        # Converte a chave digitada de hexadecimal para bytes
        chaves = bytes.fromhex(chaves)
        # Descriptografa o texto cifrado usando a chave fornecida
        texto_decifrado = descriptografar(texto_cifrado, chaves)
        # Exibe o texto decifrado, convertendo de bytes para string
        print("...Texto decifrado:", texto_decifrado.decode('utf-8'))
    elif escolha == 4:
        print("...Saindo do programa...")
        break
    escolha = menu_principal()
