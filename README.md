# CriptoGuard

Projeto simples em Python para **criptografar e descriptografar mensagens de texto** via terminal.

Este repositório foi criado durante o curso técnico e serve como base para praticar:
- modularização de código;
- manipulação de entrada/saída;
- conceitos introdutórios de segurança com chaves de criptografia.

## Como funciona

O arquivo principal (`main.py`) executa o fluxo abaixo:
1. Solicita uma mensagem ao usuário.
2. Gera/obtém uma chave com `retorna_token()`.
3. Criptografa a mensagem com `criptografar()`.
4. Pergunta se o usuário deseja descriptografar.
5. Se sim, recupera o conteúdo com `descriptografar()`.

## Estrutura atual

```text
CriptoGuard/
├── LICENSE
├── README.md
└── main.py
```

> Observação: o `main.py` importa módulos `cripto` e `descripto`. Eles não estão neste repositório no momento.

## Requisitos

- Python 3.10+ (recomendado)
- Biblioteca: `cryptography`
- Módulos locais:
	- `cripto.py` (com `retorna_token` e `criptografar`)
	- `descripto.py` (com `descriptografar`)

Instalação da dependência:

```bash
pip install cryptography
```

Ou instale pelo arquivo de requisitos:

```bash
pip install -r requirements.txt
```

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

## Exemplo de uso

```text
DIGITE A MENSAGEM QUE DESEJA CRIPTOGRAFAR: Olá mundo
MENSAGEM CRIPTOGRAFADA: b'gAAAAAB...'
DESEJA DESCRIPTOGRAFAR A MENSAGEM? (s/n): s
MENSAGEM DESCRIPTOGRAFADA: Olá mundo
```

## Boas práticas recomendadas

### 1) Organização e arquitetura
- Separar responsabilidades por módulo (`cripto`, `descripto`, `cli`).
- Evitar lógica direta no escopo global; usar `main()` e `if __name__ == "__main__":`.
- Definir nomes claros e consistentes em português ou inglês (evite mistura sem padrão).

### 2) Segurança
- Nunca versionar chaves, tokens e segredos no Git.
- Usar variáveis de ambiente para configurações sensíveis.
- Validar entradas do usuário e tratar erros de descriptografia.
- Documentar qual algoritmo/biblioteca está sendo usado e por quê.

### 3) Qualidade de código
- Adicionar tipagem com type hints.
- Criar testes unitários para os fluxos de criptografia/descriptografia.
- Adotar ferramentas como `ruff`/`flake8` e `black` para padrão de estilo.

### 4) Experiência de uso (CLI)
- Tratar respostas inválidas (`s/n`) com repetição de pergunta.
- Exibir mensagens de erro amigáveis.
- Permitir leitura de mensagem por arquivo como evolução futura.

### 5) Versionamento
- Fazer commits pequenos com mensagens descritivas.
- Manter `README` sempre atualizado com mudanças do projeto.
- Criar releases quando houver versões estáveis.

## Próximos passos sugeridos

- Incluir os arquivos `cripto.py` e `descripto.py` no repositório.
- Estruturar o projeto com pasta `src/`.
- Adicionar `requirements.txt`.
- Criar testes com `pytest`.

---

Se quiser, posso continuar e já deixar o projeto organizado com `main()` + tratamento de erros + estrutura inicial de módulos para facilitar evolução.