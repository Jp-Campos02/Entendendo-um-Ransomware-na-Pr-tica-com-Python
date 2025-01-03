from cryptography.fernet import Fernet
import os

# Gera uma chave e salva em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Carrega a chave do arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Criptografa o arquivo especificado
def criptografar_arquivo(caminho_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)
    
    with open(caminho_arquivo, "rb") as file:
        dados = file.read()

    dados_criptografados = fernet.encrypt(dados)
    
    with open(caminho_arquivo, "wb") as file:
        file.write(dados_criptografados)

# Exemplo de uso
if __name__ == "__main__":
    gerar_chave()  # Gera a chave uma vez
    caminho = input("Digite o caminho do arquivo a ser criptografado: ")
    if os.path.exists(caminho):
        criptografar_arquivo(caminho)
        print("Arquivo criptografado com sucesso!")
    else:
        print("Arquivo não encontrado.")

