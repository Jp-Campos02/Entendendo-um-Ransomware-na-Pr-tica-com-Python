import os
from encrypter import gerar_chave, criptografar_arquivo
from decrypter import descriptografar_arquivo

def criar_arquivo_teste(nome_arquivo, conteudo):
    """Cria um arquivo de teste com o conteúdo especificado."""
    with open(nome_arquivo, "w") as file:
        file.write(conteudo)

def verificar_conteudo(nome_arquivo, conteudo_esperado):
    """Verifica se o conteúdo do arquivo corresponde ao esperado."""
    with open(nome_arquivo, "r") as file:
        conteudo = file.read()
    return conteudo == conteudo_esperado

def teste_criptografia_descriptografia():
    """Executa o teste de criptografia e descriptografia."""
    # Configurações
    nome_arquivo = "teste.txt"
    conteudo_original = "Este é um teste de criptografia."
    
    # Cria o arquivo de teste
    print("Criando arquivo de teste...")
    criar_arquivo_teste(nome_arquivo, conteudo_original)
    print(f"Arquivo {nome_arquivo} criado com sucesso.")

    # Gera a chave
    print("Gerando chave de criptografia...")
    gerar_chave()

    # Criptografa o arquivo
    print("Criptografando o arquivo...")
    criptografar_arquivo(nome_arquivo)
    print("Arquivo criptografado com sucesso.")

    # Verifica se o arquivo foi alterado
    print("Verificando conteúdo criptografado...")
    with open(nome_arquivo, "r") as file:
        conteudo_criptografado = file.read()
    if conteudo_criptografado != conteudo_original:
        print("Arquivo foi criptografado com sucesso.")
    else:
        print("Erro: O conteúdo do arquivo não foi alterado.")

    # Descriptografa o arquivo
    print("Descriptografando o arquivo...")
    descriptografar_arquivo(nome_arquivo)
    print("Arquivo descriptografado com sucesso.")

    # Verifica se o conteúdo voltou ao original
    print("Verificando conteúdo descriptografado...")
    if verificar_conteudo(nome_arquivo, conteudo_original):
        print("O arquivo foi descriptografado corretamente.")
    else:
        print("Erro: O conteúdo descriptografado não corresponde ao original.")

    # Limpeza
    print("Removendo arquivos de teste...")
    os.remove(nome_arquivo)
    if os.path.exists("chave.key"):
        os.remove("chave.key")
    print("Arquivos de teste removidos com sucesso.")

# Executa o teste
if __name__ == "__main__":
    teste_criptografia_descriptografia()
