from funcoes_aes import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad 
from Crypto.Random import get_random_bytes
chaves = criar_chave()
texto_clean = b"Serafins"
criptografia = criptografar(chaves, texto_clean)
with open("Palavra.txt", "wb") as arquivo:
    arquivo.write(criptografia)
print("Texto cifrado:", criptografia)
descriptografia = descriptografar(criptografia, chaves)
print("Texto decifrado:", descriptografia.decode())

dselection = menu()
while dselection > 0 and dselection < 4: 
    if dselection == 1:
        esc1()
    elif dselection == 2:
        ler_chave = esc2()
        print("Chave lida:", ler_chave.hex())
    elif dselection == 3:
        print("Saindo do programa.")
        break
    dselection = menu()