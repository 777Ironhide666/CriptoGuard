from cryptography.fernet import Fernet


def descriptografar(mensagem_criptografada: bytes | str, key: bytes | str) -> str:
    if isinstance(key, str):
        key = key.encode("utf-8")

    if isinstance(mensagem_criptografada, str):
        mensagem_criptografada = mensagem_criptografada.encode("utf-8")

    fernet = Fernet(key)
    mensagem = fernet.decrypt(mensagem_criptografada)
    return mensagem.decode("utf-8")
