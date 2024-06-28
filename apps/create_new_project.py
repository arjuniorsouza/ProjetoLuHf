import sys
import os
from datetime import datetime
from gui.interfaces.py.NewProject import *
from apps.manage_directories import *
from apps.dialogs_interfaces import *


class CreateNewProject(QMainWindow):
    # Essas variáveis serão utilizadas para retornar, para a janela principal, o nome e o local onde o projeto foi salvo
    local_e_nome_projeto = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.nome_projeto = "Projeto " + str(datetime.now()).replace(':', '-').replace('.','_')  # O nome precisa ser
        # corrigido, pois ele possui caracteres inválidos para nome de pastas (: e .)
        # Por padrão, o local será User>Desktop
        self.local_projeto = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        # Criando o caminho do projeto (onde ele está)
        self.caminho_projeto = self.local_projeto + "\\" + self.nome_projeto

        self.ui = Ui_NewProjectWindow()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Conectando os botões as suas respectivas funções
        self.ui.btn_Close.clicked.connect(self.clique_botao)
        self.ui.btn_CreateProject.clicked.connect(self.clique_botao)
        self.ui.btn_LocalSaveProject.clicked.connect(self.clique_botao)

        # Mostrando um nome padrão no campo para inserir o nome e local do projeto
        self.ui.lineEdit_NameProject.setText(self.nome_projeto)
        self.ui.lineEdit_LocalProject.setText(self.local_projeto)



    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

    def clique_botao(self):
        # Capturando o sinal quando um botão é clicado
        btn = self.sender()

        # Obtendo o nome do botão que foi clicado
        nome_botao = btn.objectName()

        if nome_botao == "btn_Close":
            self.close()

        if nome_botao == "btn_CreateProject":
            try:
                self.nome_projeto = self.ui.lineEdit_NameProject.text()
                self.local_projeto = self.ui.lineEdit_LocalProject.text()

                # Verificando se o local onde é inserido o nome do projeto e o local onde ficará salvo estão vazios
                if not self.nome_projeto.strip():
                    self.nome_projeto = "Projeto " + str(datetime.now()).replace(':', '-').replace('.','_')

                if not self.local_projeto.strip():
                    # Se self.local_projeto estiver vazio o local padrão sera a pasta User>Desktop do PC
                    self.local_projeto = os.path.join(os.environ['USERPROFILE'], 'Desktop')

                # Chamando o método da classe GerenciarArquivos, para criar a pasta com o nome e local desejado
                GerenciarDiretorios.criar_pasta(self, self.local_projeto, self.nome_projeto)

                # Mudando os atributos nome e local da classe
                self.caminho_projeto = self.local_projeto + "/" + self.nome_projeto

                self.show_dialog_message(tipo_dialogo="Sucessful", mensagem = "Project created successfully!")
                # Enviando o nome do projeto e o local onde ele esta salvo para a janela principal
                valor_local_projeto = self.local_projeto
                valor_nome_projeto = self.nome_projeto
                self.local_e_nome_projeto.emit(valor_local_projeto, valor_nome_projeto)

                # Cria as pastas necessárias para o projeto
                # Pasta onde ficará guardado os arquivos importados
                GerenciarDiretorios.criar_pasta(self, self.caminho_projeto.replace("/", "\\"), "Original Input Data (.exp)")

                # Pasta onde ficarão os arquivos após a filragem dos dados importantes
                GerenciarDiretorios.criar_pasta(self, self.caminho_projeto.replace("/", "\\"), "Formatted Original "
                                                                                               "Data(.txt)")

                self.close()

            # Se tiver algum erro durante a criação do projeto

            except Exception as e:
                self.show_dialog_message(tipo_dialogo="Error", mensagem=f"{e}")



        if nome_botao == "btn_LocalSaveProject":
            dialog = QFileDialog()
            # Define para que seja escolhida apenas pastas
            dialog.setFileMode(QFileDialog.Directory)
            if dialog.exec():
                try:
                    # Pega o  caminho  da pasta que foi selecionada
                    self.local_projeto = dialog.selectedFiles()[0]

                except Exception as e:
                    self.show_dialog_message(tipo_dialogo="Error", mensagem=f"{e}")


            # Mostra o local selecionado no no campo label_local_projeto
            self.ui.lineEdit_LocalProject.setText(self.local_projeto)

    def show_dialog_message(self, tipo_dialogo, mensagem):
        if tipo_dialogo == "Sucessful":
            dialog = ShowDialogSucessful(mensagem)
            dialog.exec()

        if tipo_dialogo == "Error":
            dialog = ShowDialogError(mensagem)
            dialog.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CreateNewProject()
    window.show()
    sys.exit(app.exec())
