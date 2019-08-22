# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
# 
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from Inicial_ui import Ui_InicialWindow

import pyrebase 

config = {
       "apiKey": "AIzaSyAyjcUdh7IvqgTAeGHWmsnzL0Yrec3kI_s",
        "authDomain": "coffee-5ecbc.firebaseapp.com",
        "databaseURL": "https://coffee-5ecbc.firebaseio.com",
        "projectId": "coffee-5ecbc",
        "storageBucket": "coffee-5ecbc.appspot.com",
        "messagingSenderId": "834785170845",
        "appId": "1:834785170845:web:3f7b3b3a7956acd8"
}


#inicializando o app
firebase = pyrebase.initialize_app(config)


class Ui_MainWindow(object):

    def abrirJanela(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InicialWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def _on_button_clicked(self):
        email= self.inputUsuario.text()
        password = self.inputSenha.text()
        global firebase
        #Criando autenticação
        auth = firebase.auth()
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            print("Login successful")
        except :
            print("ocorreu um erro ao se logar no sistema")
            




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bemvindo = QtWidgets.QLabel(self.centralwidget)
        self.bemvindo.setGeometry(QtCore.QRect(0, 50, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bemvindo.setFont(font)
        self.bemvindo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bemvindo.setLineWidth(1)
        self.bemvindo.setMidLineWidth(2)
        self.bemvindo.setAlignment(QtCore.Qt.AlignCenter)
        self.bemvindo.setObjectName("bemvindo")
        self.sistema = QtWidgets.QLabel(self.centralwidget)
        self.sistema.setGeometry(QtCore.QRect(0, 90, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sistema.setFont(font)
        self.sistema.setAlignment(QtCore.Qt.AlignCenter)
        self.sistema.setObjectName("sistema")
        self.inputUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.inputUsuario.setGeometry(QtCore.QRect(240, 184, 361, 31))
        self.inputUsuario.setObjectName("inputUsuario")
        self.usuario = QtWidgets.QLabel(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(160, 190, 68, 19))
        self.usuario.setObjectName("usuario")
        self.senha = QtWidgets.QLabel(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(170, 240, 68, 19))
        self.senha.setObjectName("senha")
        self.inputSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.inputSenha.setGeometry(QtCore.QRect(240, 234, 361, 31))
        self.inputSenha.setMaxLength(10)
        self.inputSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputSenha.setObjectName("inputSenha")
        self._on_button_clicked()
        self.entrar = QtWidgets.QPushButton(self.centralwidget)
        self.entrar.setGeometry(QtCore.QRect(270, 320, 121, 41))
        self.entrar.setObjectName("entrar")

        self.entrar.clicked.connect(self._on_button_clicked)
        self.entrar.clicked.connect(self.abrirJanela)

        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(420, 320, 121, 41))
        self.cancelar.setObjectName("cancelar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bemvindo.setText(_translate("MainWindow", "Bem vindo(a)"))
        self.sistema.setText(_translate("MainWindow", "Sistema de Cadastro de Livros"))
        self.usuario.setText(_translate("MainWindow", "Usuário:"))
        self.senha.setText(_translate("MainWindow", "Senha:"))
        self.entrar.setText(_translate("MainWindow", "Entrar"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

