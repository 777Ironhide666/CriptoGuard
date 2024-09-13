from cripto import retorna_token, criptografar
from descripto import descriptografar

mensagem_original = input("DIGITE A MENSAGEM QUE DESEJA CRIPTOGRAFAR: ")

key = retorna_token()

mensagem_protegida = criptografar(mensagem_original, key)
print("MENSAGEM CRIPTOGRAFADA: ", mensagem_protegida)


resposta = input("DESEJA DESCRIPTOGRAFAR A MENSAGEM? (s/n): ")
if resposta.lower() == 's':
    mensagem_recuperada = descriptografar(mensagem_protegida, key)
    print("MENSAGEM DESCRIPTOGRAFADA:", mensagem_recuperada)
