def perguntar_descriptografia() -> str:
    while True:
        resposta = input("DESEJA DESCRIPTOGRAFAR A MENSAGEM? (s/n): ").strip().lower()
        if resposta in {"s", "n"}:
            return resposta
        print("Resposta inválida. Digite apenas 's' ou 'n'.")


def main() -> None:
    try:
        from cripto import retorna_token, criptografar
        from descripto import descriptografar
    except ImportError as erro:
        print(f"Erro ao importar módulos necessários: {erro}")
        print("Verifique se os arquivos 'cripto.py' e 'descripto.py' existem no projeto.")
        return

    mensagem_original = input("DIGITE A MENSAGEM QUE DESEJA CRIPTOGRAFAR: ").strip()
    if not mensagem_original:
        print("Nenhuma mensagem informada. Encerrando.")
        return

    try:
        key = retorna_token()
        mensagem_protegida = criptografar(mensagem_original, key)
    except Exception as erro:
        print(f"Falha ao criptografar a mensagem: {erro}")
        return

    print("MENSAGEM CRIPTOGRAFADA:", mensagem_protegida)

    resposta = perguntar_descriptografia()
    if resposta == "s":
        try:
            mensagem_recuperada = descriptografar(mensagem_protegida, key)
            print("MENSAGEM DESCRIPTOGRAFADA:", mensagem_recuperada)
        except Exception as erro:
            print(f"Falha ao descriptografar a mensagem: {erro}")


if __name__ == "__main__":
    main()
