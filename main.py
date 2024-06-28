import sys
import os

# Importando os arquivos de interface gráfica
from gui.interfaces.py.MainWindow import *
from apps.create_new_project import *
from apps.dialogs_interfaces import *
from apps.manage_directories import *
from apps.manipulate_data_files import *


# Classe principal da aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Atributos relacionados a interface
        self.animation = None
        self.show_new_project_window = None

        # Atributos relacionados ao projeto
        self.local_projeto_criado = None
        self.nome_projeto_criado = None
        self.caminhos_originais_arquivos_exp = None  # Guarda o caminho de origem dos arquivos EXP (de onde foram copiados)
        self.caminho_pasta_Original_Input_Data_exp = None  # Caminho da pasta "Original Input Data (.exp)
        self.caminhos_arquivos_importados_exp = []  # Guarda o caminho dos arquivos exp
        self.caminho_pasta_Formatted_Original_Data_txt = None  # Caminho da pasta "Formatted Original Data (.txt)
        self.caminhos_arquivos_importados_txt = []  # Guarda o caminho dos arquivos txt
        self.dataframe_arquivos_txt = {}  # Dataframe para guardar os dados dos arquivos txt
        self.nomes_arquivos_txt = []  # Guarda apenas o nome dos arquivos, não o caminho completo

        # Setup a Main Window
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Retirando as bordas da janela padrão do Windows
        # Esse objeto é responsável por adicionar a função de redimensionar a janela no canto inferior direito
        QSizeGrip(self.ui.frame_size_grip)

        # Remove a barra de títulos padrão do Windows
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Definindo a posição inicial do mouse (necessário para os eventos onde a tela é movida de posição)
        self.drag_start_position = None

        # Conectando os elementos com seus respectivos métodos
        # Conectando a função que irá expandir/retrair o menu quando ele for clicado
        self.ui.toggleButton.clicked.connect(self.expandir_menu)

        # Conectando os botões do menu da página "Home" com suas respectivas funções
        self.ui.btn_NewProjectHome.clicked.connect(self.clique_botao)
        self.ui.btn_OpenProjectHome.clicked.connect(self.clique_botao)
        self.ui.btn_ExportProjectHome.clicked.connect(self.clique_botao)
        self.ui.btn_SettingsHome.clicked.connect(self.clique_botao)

        # Conectando os botões do menu esquerdo com suas respectivas funções
        self.ui.btn_Home.clicked.connect(self.clique_botao)
        self.ui.btn_NewProject.clicked.connect(self.clique_botao)
        self.ui.btn_OpenProject.clicked.connect(self.clique_botao)
        self.ui.btn_ImportFiles.clicked.connect(self.clique_botao)
        self.ui.btn_AddMoreFiles.clicked.connect(self.clique_botao)
        self.ui.btn_ShowData.clicked.connect(self.clique_botao)
        self.ui.btn_DefBackgroundSignal.clicked.connect(self.clique_botao)
        self.ui.btn_Settings.clicked.connect(self.clique_botao)

        # Botoões responsáveis por redimensionar e fechar a interface
        self.ui.btn_CloseApp.clicked.connect(self.clique_botao)
        self.ui.btn_RestaureSizeApp.clicked.connect(self.clique_botao)
        self.ui.btn_MinimizeApp.clicked.connect(self.clique_botao)

        self.show()

    # Esses métodos são responsáveis por redimensionar e movimentar a janela
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.drag_start_position is not None:
            self.move(event.globalPosition().toPoint() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = None
            event.accept()

    # Função que irá expandir e retrair o menu esquerdo
    def expandir_menu(self):
        # Obtendo a largura do menu esquerdo
        largura_menu_esquerdo = self.ui.leftMenuBg.width()

        largura_padrao = 60

        if largura_menu_esquerdo == 60:
            largura_padrao = 200

        # Animando a transição
        self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
        self.animation.setDuration(900)
        self.animation.setStartValue(largura_menu_esquerdo)
        self.animation.setEndValue(largura_padrao)
        self.animation.setEasingCurve(QEasingCurve.OutCirc)
        self.animation.start()

    # Essa função pega o nome do botão que foi clicado e conecta a sua respectiva função
    def clique_botao(self):
        # Capturando o sinal quando um botão é clicado
        btn = self.sender()

        # Obtendo o nome do botão que foi clicado
        nome_botao = btn.objectName()

        # Mostra a página inicial da aplicação
        if nome_botao == "btn_Home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_Home)

        # Minimiza a janela da aplicação
        if nome_botao == "btn_CloseApp":
            self.close()

        # Restaura o tamanho da janela da aplicação
        if nome_botao == "btn_RestaureSizeApp":

            # Se a janela estiver no seu tamanho máximo, ele volta para o seu tamanho mínimo definido
            if self.isMaximized():
                self.showNormal()

            # Se a janela estiver no seu tamanho mínimo definido, ela é maximizada
            else:
                self.showMaximized()

        # Fecha a aplicação
        if nome_botao == "btn_MinimizeApp":
            self.showMinimized()

        # Criando um novo projeto
        if nome_botao == "btn_NewProject" or nome_botao == "btn_NewProjectHome":
            if self.local_projeto_criado is None and self.nome_projeto_criado is None:
                self.mostrar_interface_novo_projeto()

            else:
                dialogo_interativo = ShowDialogInteractive("There is a project underway. Do you want to start another "
                                                           "one?")
                dialogo_interativo.opcaoSelecionada.connect(self.obter_op_selecionada_novo_projeto)
                dialogo_interativo.exec()

        if nome_botao == "btn_ImportFiles":
            # Verificando se já existe um projeto criado
            if self.local_projeto_criado is not None and self.nome_projeto_criado is not None:
                if len(self.caminhos_arquivos_importados_exp) == 0:
                    self.importar_arquivos_exp()

                else:
                    self.mostrar_dialog_box(tipo_dialogo="Info", mensagem="There is already a set of imported files. "
                                                                          "To add more files, use the 'Add Files' "
                                                                          "option!")
            else:
                self.mostrar_dialog_box(tipo_dialogo="Info",
                                        mensagem="Before importing any data, create a project first!")

        if nome_botao == "btn_AddMoreFiles":
            # Verificando se há um projeto criado
            if self.local_projeto_criado is not None and self.nome_projeto_criado is not None:
                # Caso tenha um projeto criado, é verificado se algum arquivo já foi importado
                # Se sim, a função para adicionar mais arquivos é chamada
                if len(self.caminhos_arquivos_importados_exp) > 0:
                    self.importar_arquivos_add()

                # Se não, é chamada a função de importar arquivos
                else:
                    self.importar_arquivos_exp()

            else:
                self.mostrar_dialog_box(tipo_dialogo="Info",
                                        mensagem="Before importing any data, create a project first!")

        if nome_botao == "btn_ShowData":
            self.ui.stackedWidget.setCurrentWidget(self.ui.pg_SeeData)

    def mostrar_interface_novo_projeto(self):
        self.show_new_project_window = CreateNewProject()
        # Muda os atributos da classe principal, pois a janela do novo projeto pega o
        # nome e o local do projeto escolhido pelo usuário
        self.show_new_project_window.local_e_nome_projeto.connect(self.alterar_atributos_nome_e_local)
        self.show_new_project_window.show()

    def alterar_atributos_nome_e_local(self, valor_local_projeto, valor_nome_projeto):
        self.local_projeto_criado = valor_local_projeto
        self.nome_projeto_criado = valor_nome_projeto
        self.ui.titleProject.setText(self.nome_projeto_criado)

    def obter_op_selecionada_novo_projeto(self):
        self.mostrar_interface_novo_projeto()

    def importar_arquivos_exp(self):
        try:
            # É preciso copiar os arquivos da pasta original para a pasta "Original Input Data (.exp)"
            # Para isso, obtemos os caminhos originais dos arquivos no formato ".exp"
            caminhos_arquivos_exp = self.selecionar_arquivos()
            num_arq_importados = len(caminhos_arquivos_exp)

            if caminhos_arquivos_exp is not None:
                self.caminhos_originais_arquivos_exp = caminhos_arquivos_exp

                # Depois, iremos copiar estes arquivos para a pasta "Original Input Data (.exp)"
                # Obtendo o caminho da pasta de destino
                self.caminho_pasta_Original_Input_Data_exp = (self.local_projeto_criado + "/" +
                                                              self.nome_projeto_criado + "/Original Input Data (.exp)")
                copiar_arquivos_exp = GerenciarDiretorios()
                copiar_arquivos_exp.copiar_arquivos(self.caminhos_originais_arquivos_exp,
                                                    self.caminho_pasta_Original_Input_Data_exp)

                # Depois, precisamos obter os caminhos dos arquivos originais copiados para a pasta "Original
                # Input Data (.exp)" para realizar a filtragem dos dados
                self.caminhos_arquivos_importados_exp = copiar_arquivos_exp.obter_caminhos_arquivos(
                    self.caminho_pasta_Original_Input_Data_exp)

                # Chamando a função que irá filtrar os dados originais, eliminando os dados desnecessários
                # Obtendo o caminho da pasta onde os arquivos txt ficarão guardados
                self.caminho_pasta_Formatted_Original_Data_txt = (self.local_projeto_criado + "/" +
                                                                  self.nome_projeto_criado + "/Formatted Original Data(.txt)")
                manipular_arquivos_exp = ManipulateData()
                manipular_arquivos_exp.excluir_dados_inuteis(self.caminhos_arquivos_importados_exp,
                                                             self.caminho_pasta_Formatted_Original_Data_txt)

                # Agora é necessário criar os dataframes com os dados dos arquivos txt. Eles ficaram guardados em um
                # dicionário.
                # Primeiro obtemos os caminhos de cada arquivo txt gerado, que estão na pasta Formatted
                # Original Data(.txt)
                caminhos_arquivos_txt = GerenciarDiretorios()
                self.caminhos_arquivos_importados_txt = caminhos_arquivos_txt.obter_caminhos_arquivos(
                    self.caminho_pasta_Formatted_Original_Data_txt)
                # Depois, passamos esses caminhos para o método que irá criar os dataframes
                gerar_dataframes = ManipulateData()
                self.dataframe_arquivos_txt = gerar_dataframes.criar_dataframes_arquivos_txt(
                    self.caminhos_arquivos_importados_txt)

                # Iremos precisar também dos nomes de cada arquivo, para servir de referência em outras funções
                self.nomes_arquivos_txt = [os.path.basename(caminho) for caminho in
                                           self.caminhos_arquivos_importados_txt]

                # Com os dados ja armazenados em dataframes, é necessário chamar a função responsável
                # por mostrar os nomes dos arquivos importados nas QListWidget da interface
                self.preencher_q_list_widget(self.ui.listWidget_FilesStandard)
                self.preencher_q_list_widget(self.ui.listWidget_FilesSamples)

                self.mostrar_dialog_box(tipo_dialogo="Sucessful", mensagem=f"{num_arq_importados} files were imported!")

            # Caso nenhum arquivo tenha sido selecionado
            else:
                self.mostrar_dialog_box(tipo_dialogo="Info", mensagem="No file selected!")

        except Exception as e:
            self.mostrar_dialog_box(tipo_dialogo="Error", mensagem=str(e))

    def importar_arquivos_add(self):
        try:
            caminho_pasta_exp = self.caminho_pasta_Original_Input_Data_exp + "/"
            caminho_pasta_txt = self.caminho_pasta_Formatted_Original_Data_txt + "/"

            # É preciso copiar os arquivos da pasta original para a pasta "Original Input Data (.exp)"
            # Para isso, obtemos os caminhos originais dos arquivos no formato ".exp"
            caminhos_arquivos_exp = self.selecionar_arquivos()
            numero_arquivos_exp_selecionados = len(caminhos_arquivos_exp)

            if caminhos_arquivos_exp is not None:
                # É preciso verificar se não há nenhum arquivo importado com o mesmo nome de algum arquivo importado
                # adicionalmente (para evitar duplicações)
                # Primeiro, obtemos os nomes de cada arquivo importado adicionalmente,
                nomes_arq_add = [os.path.basename(caminho) for caminho in caminhos_arquivos_exp]

                # Depois obtemos o nome dos arquivos exp já importados anteriormente
                nomes_arq_exp = [os.path.basename(caminho) for caminho in self.caminhos_originais_arquivos_exp]

                # Agora comparamos as duas listas, para ver se algum item selecionado adicionalmente já foi importado
                itens_replicados_import = self.comparar_itens_replicados(nomes_arq_add, nomes_arq_exp)

                itens_nao_duplicados_import = [item for item in nomes_arq_add if item not in itens_replicados_import]
                numero_arquivos_nao_duplicados = len(itens_nao_duplicados_import)

                # Agora precisamos obter o caminho original dos arquivos não duplicados
                # Filtra os caminhos cujos nomes de arquivos estão na lista nomes_arquivo
                caminhos_nao_duplicados = [caminho for caminho in caminhos_arquivos_exp if os.path.basename(caminho) in itens_nao_duplicados_import]
                caminhos_arquivos_exp = caminhos_nao_duplicados


                self.caminhos_originais_arquivos_exp.extend(caminhos_arquivos_exp)

                # Primeiro, copiamos os arquivos selecionados para a pasta "Original Input Data (.exp)"
                copiar_arquivos_exp = GerenciarDiretorios()
                copiar_arquivos_exp.copiar_arquivos(caminhos_arquivos_exp, self.caminho_pasta_Original_Input_Data_exp)

                # Agora precisamos obter os caminhos dos arquivos adicionais para que eles sejam filtrados.
                # Não pode ser feito pegando os caminhos da pasta "Original Input Data (.exp)", pois implicaria
                # processar novamente os arquivos importados originalmente
                # Obtemos apenas o caminho dos arquivos importados adicionalmente
                caminhos_arq_adicionais_exp = [os.path.join(caminho_pasta_exp, os.path.basename(caminho)) for caminho in
                                               caminhos_arquivos_exp]

                # Adicionando os caminhos dos itens selecionados adicionalmente ao atributo
                # self.caminhos_arquivos_importados_exp
                self.caminhos_arquivos_importados_exp.extend(caminhos_arq_adicionais_exp)

                # Agora chamamos a função para filtrar os dados, excluindo as linhas inúteis dos arquivos, e criando
                # os arquivos txt
                manipular_dados_exp_add = ManipulateData()
                manipular_dados_exp_add.excluir_dados_inuteis(caminhos_arq_adicionais_exp,
                                                              self.caminho_pasta_Formatted_Original_Data_txt)

                # Agora iremos gerar os dataframes dos arquivos adicionais
                # Não pode ser feito pegando os caminhos da pasta "Formatted original Data (.txt)", pois implicaria
                # processar novamente os arquivos importados originalmente
                # Obtemos o caminho apenas o caminho dos arquivos importados adicionalmente

                caminhos_arq_adicionais_txt = [os.path.join(caminho_pasta_txt, os.path.basename(caminho)) for caminho in
                                               caminhos_arquivos_exp]

                # Substitui .exp por .txt em todos os caminhos da lista, pois em caminhos_arq.adicionais_txt a
                # extensão do arquivo é .exp (o que não pode acontecer)
                novos_caminhos = [os.path.splitext(caminho)[0] + '.txt' for caminho in caminhos_arq_adicionais_txt]
                caminhos_arq_adicionais_txt = novos_caminhos

                # Agora é necessário verificar se alguns dos novos arquivos selecionados já haviam sido selecionados
                # antes Para isso, precisamos compara as listas self.caminhos_arquivos_importados_exp e
                # caminhos_arquivos_exp
                itens_ja_adicionados_txt = self.comparar_itens_replicados(caminhos_arq_adicionais_txt,
                                                                          self.caminhos_arquivos_importados_txt)

                # Excluindo os itens importados mais de uma vez
                itens_nao_duplicados_txt = [item for item in caminhos_arq_adicionais_txt if
                                            item not in itens_ja_adicionados_txt]

                caminhos_arq_adicionais_txt = itens_nao_duplicados_txt

                # Atualizando o atributo self.caminhos_arquivos_importados_txt com os caminhos dos novos arquivos
                self.caminhos_arquivos_importados_txt.extend(caminhos_arq_adicionais_txt)
                # Atualizando o atributo que guarda o nome dos arquivos txt
                nomes_arquivos = [os.path.basename(caminho) for caminho in caminhos_arq_adicionais_txt]
                self.nomes_arquivos_txt.extend(nomes_arquivos)

                # Agora vamos criar o dataframe dos novos arquivos selecionados
                gerar_dataframes = ManipulateData()
                dataframes_novos = gerar_dataframes.criar_dataframes_arquivos_txt(caminhos_arq_adicionais_txt)

                # Atualizando o conjunto de dataframes que contém os dados do projeto
                self.dataframe_arquivos_txt.update(dataframes_novos)

                # Atualizando as QListWidget
                self.preencher_q_list_widget(self.ui.listWidget_FilesStandard)
                self.preencher_q_list_widget(self.ui.listWidget_FilesSamples)

                self.mostrar_dialog_box(tipo_dialogo="Sucessful", mensagem=f"{numero_arquivos_nao_duplicados}/{numero_arquivos_exp_selecionados}"
                                                                      f" selected files were imported!")

        except Exception as e:
            self.mostrar_dialog_box(tipo_dialogo="Error", mensagem=e)

    def selecionar_arquivos(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)

        # Mostra apenas os arquivos com extensão ".exp"
        file_dialog.setNameFilter("Arquivos de Texto (*.exp);")

        if file_dialog.exec():
            # Obtenha os arquivos selecionados
            arquivos_selecionados = file_dialog.selectedFiles()

            return arquivos_selecionados

    def preencher_q_list_widget(self, nome_q_list_widget):
        # Primeiro precisamos obter o nome de cada arquivo importado
        # Para isso precisamos extraí-los dos caminhos presentes em self.caminhos_arquivos_importados_txt
        # Verificando se existem itens na lista. Se sim, eles são excluídos
        if nome_q_list_widget.count() > 0:
            nome_q_list_widget.clear()

        for arquivo in self.nomes_arquivos_txt:
            list_item = QListWidgetItem(arquivo)
            nome_q_list_widget.addItem(list_item)

    # Este método compra duas listas e verifica se existe algum arquivo que aparecem em ambas
    def comparar_itens_replicados(self, lista_adicional, lista_original):
        itens_replicados = []
        for item_adicional in lista_adicional:
            for item_original in lista_original:
                if item_adicional == item_original:
                    itens_replicados.append(item_adicional)

        return itens_replicados

    def mostrar_dialog_box(self, tipo_dialogo, mensagem):
        if tipo_dialogo == "Info":
            dialogo = ShowDialogInfo(mensagem)
            dialogo.exec()

        if tipo_dialogo == "Sucessful":
            dialogo = ShowDialogSucessful(mensagem)
            dialogo.exec()

        if tipo_dialogo == "Error":
            dialogo = ShowDialogError(mensagem)
            dialogo.exec()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
