# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicial.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Buscar_ui import Ui_BuscarWindow
from Cadastro_ui import Ui_CadastroWindow

class Ui_InicialWindow(object):

    def JanelaBuscar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BuscarWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def JanelaCadastro(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CadastroWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, InicialWindow):
        InicialWindow.setObjectName("InicialWindow")
        InicialWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        InicialWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(InicialWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boasvindas = QtWidgets.QLabel(self.centralwidget)
        self.boasvindas.setGeometry(QtCore.QRect(60, 70, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(12)
        self.boasvindas.setFont(font)
        self.boasvindas.setObjectName("boasvindas")
        self.buscarlivro = QtWidgets.QPushButton(self.centralwidget)
        self.buscarlivro.setGeometry(QtCore.QRect(120, 170, 571, 71))
        self.buscarlivro.setObjectName("buscarlivro")

        self.buscarlivro.clicked.connect(self.JanelaBuscar)

        self.cadastrarlivro = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrarlivro.setGeometry(QtCore.QRect(120, 250, 571, 71))
        self.cadastrarlivro.setObjectName("cadastrarlivro")

        self.cadastrarlivro.clicked.connect(self.JanelaCadastro)

        self.sair = QtWidgets.QPushButton(self.centralwidget)
        self.sair.setGeometry(QtCore.QRect(120, 330, 571, 71))
        self.sair.setObjectName("sair")

        InicialWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InicialWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
        self.menubar.setObjectName("menubar")
        InicialWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InicialWindow)
        self.statusbar.setObjectName("statusbar")
        InicialWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InicialWindow)
        QtCore.QMetaObject.connectSlotsByName(InicialWindow)

    def retranslateUi(self, InicialWindow):
        _translate = QtCore.QCoreApplication.translate
        InicialWindow.setWindowTitle(_translate("InicialWindow", "InicialWindow"))
        self.boasvindas.setText(_translate("InicialWindow", "Olá Usuário"))
        self.buscarlivro.setText(_translate("InicialWindow", "Buscar Livro"))
        self.cadastrarlivro.setText(_translate("InicialWindow", "Cadastrar Livro"))
        self.sair.setText(_translate("InicialWindow", "Sair"))


if __name__ == "__inicial__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InicialWindow = QtWidgets.QMainWindow()
    ui = Ui_InicialWindow()
    ui.setupUi(InicialWindow)
    InicialWindow.show()
    sys.exit(app.exec_())

