import base64
def codificacao(arquivo1, arquivo2):
    with open(arquivo1, 'rb') as imagem:
        b1 = imagem.read()
        b64 = base64.b64encode(b1)
        strs = b64.decode('utf-8')
    print("Salvando em arquivo .txt")
    with open(arquivo2, 'w') as base64_salva:
        base64_salva.write(strs)
    print("Arquivo salvo com sucesso")

def decodificacao(arquivo1, arquivo2):
    with open(arquivo1, 'r') as li_base64:
        lido = li_base64.read()
        binarios = base64.b64decode(lido)
    with open(arquivo2, 'wb') as recuperada:
        recuperada.write(binarios)