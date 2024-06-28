import os
import pandas as pd
from apps.dialogs_interfaces import *

class ManipulateData():
    palavra_indicadora_inicio = "Cycle"
    palavra_indicadora_final = "Cup"
    def excluir_dados_inuteis(self, arquivos_exp, local_salvamento):
        try:
            for c in range(0, len(arquivos_exp)):
                # Abrindo o arquivo original (da pasta data)
                arquivo_atual = arquivos_exp[c]
                with open(arquivo_atual, "r") as arquivo:
                    linhas = arquivo.readlines()

                # Encontrando a linha a partir da qual os dados são necessários (os dados das linhas anteriores serão
                # apagados)
                comeco_dados_uteis = 0
                fim_dados_uteis = 0
                for i in range (0, len(linhas)):
                    if self.palavra_indicadora_inicio in linhas[i]:
                        comeco_dados_uteis = i+1

                for j in range(len(linhas)-1, -1, -1):
                    if self.palavra_indicadora_final in linhas[j]:
                        fim_dados_uteis = j

                # Agora é criado um novo arquivo txt, apenas com os dados úteis
                # Criando um novo arquivo, no formato txt, que ficará salvo na pasta "Formatted Original Data(.txt)
                nome_arquivo = local_salvamento + "/" + f"{os.path.basename(arquivo_atual).replace('.exp', '')}.txt"
                with open(nome_arquivo, 'w') as arquivo_destino:
                    for numero_linha, linha in enumerate(linhas, start=1):
                        if comeco_dados_uteis <= numero_linha <= fim_dados_uteis:
                            arquivo_destino.write(linha)

        except Exception as e:
            self.mostrar_dialog_box(tipo_dialogo="Error", mensagem=e)

    def criar_dataframes_arquivos_txt(self, caminhos_arquivos):
        dataframes = {}
        for arquivo in caminhos_arquivos:

            colunas = ["Cycle", "172Yb", "177Hf", "178Hf", "179Hf", "180Hf", "178Hf/177Hf (1)", "180Hf/177Hf (2)",
                       "179Hf/177Hf (3)", "176Hf/177Hf (5)", "176Hf/177Hf (6)", "175Lu/177Hf (8)", "175Lu/177Hf (8)",
                       "173Yb/177Hf (9)", "172Yb/177Hf (10)", "172Yb/177Hf (10)"]

            dataframes[os.path.basename(arquivo)] = pd.read_csv(arquivo, delimiter='\t', usecols=colunas)

            # Substituir NaN por 0
            dataframes[os.path.basename(arquivo)].fillna(0, inplace=True)

        return dataframes

    def mostrar_dialog_box(self, tipo_dialogo, mensagem):
        if tipo_dialogo == "Info":
            dialogo = ShowDialogInfo(mensagem)
            dialogo.exec()

        if tipo_dialogo == "Error":
            dialogo = ShowDialogError(mensagem)
            dialogo.exec()





