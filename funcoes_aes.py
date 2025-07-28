from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def criar_chave():
    chave = get_random_bytes(16)  # AES-128, 16 bytes = 128 bits
    return chave

def criptografar(chave, texto):
    texto_padded = pad(texto, 16)
    aes = AES.new(chave, AES.MODE_ECB) 
    texto_cifrado = aes.encrypt(texto_padded)
    return texto_cifrado  # Retorna o texto cifrado

def descriptografar(texto_cifrado, chave):
    aes = AES.new(chave, AES.MODE_ECB)
    texto_decifrado = unpad(aes.decrypt(texto_cifrado), 16) 
    return texto_decifrado

def menu():
    print("1. Guardar chave")
    print("2. Mostrar chave")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def esc1():
    with open("chave.bin", "wb") as arquivo:
        chave = criar_chave()
        arquivo.write(chave)
def esc2():
    with open("chave.bin", "rb") as arquivo:
        chave_lida = arquivo.read()
    return chave_lida

def menu_principal():
    print("1. Criptografar texto em AES")
    print("2. Exibir chave AES")
    print("3. Descriptografar texto em AES")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao