from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

chave = b"LUCASLOU"  # 8 bytes
des = DES.new(chave, DES.MODE_ECB)
texto_branco = pad(b"Santos futebol clube", 8) # Preenchimento para múltiplo de 8 bytes
texto_criptografado = des.encrypt(texto_branco)
texto_decifrado = unpad(des.decrypt(texto_criptografado), 8)
print(f"Texto descriptografado: {texto_decifrado.decode()}")

# Explicação:
# 1. A chave do DES precisa ter exatamente 8 bytes, por isso foi usada b"LUCASLOU".
# 2. O texto a ser criptografado também precisa ser bytes e múltiplo de 8 em tamanho.
#    Por isso, usamos pad() para preencher o texto até o próximo múltiplo de 8.
# 3. O texto é criptografado normalmente.
# 4. Para descriptografar, usamos unpad() para remover o preenchimento extra.
# 5. Por fim, o texto descriptografado é convertido de bytes para string com decode().

# O módulo Crypto.Util.Padding e as funções pad, unpad são necessários porque:
# - O algoritmo DES exige que o texto a ser criptografado tenha tamanho múltiplo de 8 bytes.
# - pad() adiciona bytes extras ao texto para garantir esse tamanho.
# - unpad() remove esses bytes extras após a descriptografia, recuperando o texto original.
# Sem esse preenchimento, a criptografia/descriptografia com DES pode gerar erro ou resultado incorreto.

# O método .decode() é usado porque, após a descriptografia e remoção do padding,
# o resultado ainda está em formato de bytes. Para exibir como texto legível (string),
# é necessário converter de bytes para string usando .decode().
# Exemplo:
# texto_decifrado = b'Santos futebol clube'
# texto_decifrado.decode() -> 'Santos futebol clube'

# O texto branco foi "padded" (preenchido) porque o algoritmo DES exige que o tamanho do texto a ser criptografado
# seja um múltiplo exato de 8 bytes. Se o texto não tiver esse tamanho, a função pad() adiciona bytes extras
# ao final para completar o bloco. Isso garante que a criptografia funcione corretamente e sem erros.

# O prefixo b"" indica que o texto está em formato de bytes, não string comum.
# O algoritmo DES (e as funções pad/unpad) trabalham apenas com bytes, não com strings.
# Por isso, é necessário usar b"Santos futebol clube" em vez de "Santos futebol clube".
# Se fosse uma string comum, ocorreria erro ao tentar criptografar.

# O decode() no final converte o texto de bytes (ex: b'Santos futebol clube') para string normal (ex: 'Santos futebol clube').
# Isso permite exibir o texto descriptografado de forma legível no print.
