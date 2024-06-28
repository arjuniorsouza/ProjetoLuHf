import os
import shutil


class GerenciarDiretorios:

    def __init__(self):
        super().__init__()

    # Esse método cria uma pasta sempre que ele for chamado
    def criar_pasta(self, local, nome_pasta):
        caminho = os.path.join(local, nome_pasta)
        os.makedirs(caminho)

    # Verfica se uma pasta existe
    def verificar_pasta(self, nome_pasta):
        # Verifica se o caminho existe e é uma pasta
        if os.path.exists(nome_pasta) and os.path.isdir(nome_pasta):
            return True

        else:
            return False

    # Copia um arquivo para um destino
    def copiar_arquivos(self, caminho_origem, caminho_destino):
        # Os argumentos precisam ser do tipo lista
        for c in range(0, len(caminho_origem)):
            caminho_original = caminho_origem[c]
            caminho_final = caminho_destino
            shutil.copy(caminho_original, caminho_final)

    # Apaga todos os arquivos de uma pasta
    def limpar_diretório(self, caminho_diretorio):
        # Listar todos os arquivos no diretório
        arquivos = os.listdir(caminho_diretorio)

        # Iterar sobre os arquivos e excluí-los
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_diretorio, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)

    # Esta função obtém os caminhos dos arquivos presentes em uma pasta
    def obter_caminhos_arquivos(self, caminho_pasta):
        caminhos_arquivos = []
        for arquivo in os.listdir(caminho_pasta):
            caminho_arquivo = caminho_pasta + "/" + arquivo
            if os.path.isfile(caminho_arquivo):
                caminhos_arquivos.append(caminho_arquivo)

        return caminhos_arquivos


