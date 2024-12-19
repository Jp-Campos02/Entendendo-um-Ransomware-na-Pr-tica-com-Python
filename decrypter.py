from cryptography.fernet import Fernet
import os

# Carrega a chave do arquivo
def carregar_chave():
    return open("chave.key", "rb").read()

# Descriptografa o arquivo especificado
def descriptografar_arquivo(caminho_arquivo):
    chave = carregar_chave()
    fernet = Fernet(chave)
    
    with open(caminho_arquivo, "rb") as file:
        dados_criptografados = file.read()

    dados = fernet.decrypt(dados_criptografados)
    
    with open(caminho_arquivo, "wb") as file:
        file.write(dados)

# Exemplo de uso
if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo a ser descriptografado: ")
    if os.path.exists(caminho):
        descriptografar_arquivo(caminho)
        print("Arquivo descriptografado com sucesso!")
    else:
        print("Arquivo não encontrado.")
