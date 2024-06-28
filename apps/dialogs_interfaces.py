from gui.interfaces.py.DialogSuccessful import *
from gui.interfaces.py.DialogError import *
from gui.interfaces.py.DialogInfo import *
from gui.interfaces.py.DialogWarning import *
from qt_core import *


class ShowDialogSucessful(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.mensagem = mensagem

        self.ui = Ui_DialogSucessful()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Passando a mensagem para a janela
        self.ui.label_message.setText(self.mensagem)


        # Adicionando as funções aos botões
        self.ui.btn_Close.clicked.connect(self.close_window)
        self.ui.btn_ok.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


class ShowDialogError(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogErro()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Passando a mensagem para a janela
        self.ui.label_message.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_Close.clicked.connect(self.close_window)
        self.ui.btn_Ok.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()

class ShowDialogInfo(QDialog):
    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogInfo()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Passando a mensagem para a janela
        self.ui.label_message.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_Close.clicked.connect(self.close_app)
        self.ui.btn_ok.clicked.connect(self.close_app)

    def close_app(self):
        self.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()


class ShowDialogInteractive(QDialog):
    opcaoSelecionada = Signal(str)

    def __init__(self, mensagem):
        super().__init__()

        self.ui = Ui_DialogInterativa()
        self.ui.setupUi(self)

        # Oculta a barra de títulos
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Passando a mensagem para a janela
        self.ui.label_message.setText(mensagem)

        # Adicionando as funções aos botões
        self.ui.btn_Close.clicked.connect(self.close)
        self.ui.btn_Yes.clicked.connect(self.enviar_sinal)
        self.ui.btn_No.clicked.connect(self.close)

    def enviar_sinal(self):
        # Capturando o botão que enviou o sinal(foi clicado)
        btn = self.sender()

        # Pegando o nome do botão que foi clicado
        nome_botao = btn.objectName()

        if nome_botao == "btn_Yes":
            self.opcaoSelecionada.emit("Sim")
            self.close()
            self.accept()


    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()