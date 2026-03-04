from cryptography.fernet import Fernet


def retorna_token() -> bytes:
    return Fernet.generate_key()


def criptografar(mensagem: str, key: bytes | str) -> bytes:
    if not isinstance(mensagem, str):
        raise TypeError("A mensagem deve ser uma string.")

    if isinstance(key, str):
        key = key.encode("utf-8")

    fernet = Fernet(key)
    return fernet.encrypt(mensagem.encode("utf-8"))
