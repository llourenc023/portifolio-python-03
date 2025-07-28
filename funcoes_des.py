from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
def criar_chave_des():
    chave = get_random_bytes(8)  # DES, 8 bytes = 64 bits
    return chave
def criptografar_des(chave, texto_padrao):
    texto_padded = pad(texto_padrao, 8)
    des = DES.new(chave, DES.MODE_ECB) 
    texto_cifrado = des.encrypt(texto_padded)
    return texto_cifrado  # Retorna o texto cifrado
def descriptografar_des(chave, texto_cifrado):
    des = DES.new(chave, DES.MODE_ECB)
    texto_decifrado = unpad(des.decrypt(texto_cifrado), 8) 
    return texto_decifrado  # Retorna o texto decifrado