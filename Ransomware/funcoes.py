from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad  
def criptando(arquivo, chave):
    aes = AES.new(chave, AES.MODE_ECB)
    with open(arquivo, 'rb') as file:
        dentro_doarquivo = pad(file.read(), AES.block_size)
        cifrado = aes.encrypt(dentro_doarquivo)
        print("Arquivo criptografado com sucesso!")
    with open(arquivo, 'wb') as file:
        file.write(cifrado)
        print("Arquivo original excluído e substituído pelo criptografado!")

