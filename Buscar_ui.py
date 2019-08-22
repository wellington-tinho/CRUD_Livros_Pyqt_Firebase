# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Buscar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Resultado_ui import Ui_ResultadoWindow

class Ui_BuscarWindow(object):

    def JanelaResultado(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ResultadoWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, BuscarWindow):
        BuscarWindow.setObjectName("BuscarWindow")
        BuscarWindow.resize(886, 660)
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        BuscarWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(BuscarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cadastro = QtWidgets.QLabel(self.centralwidget)
        self.cadastro.setGeometry(QtCore.QRect(30, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cadastro.setFont(font)
        self.cadastro.setObjectName("cadastro")
        self.Titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(230, 220, 561, 41))
        self.Titulo.setObjectName("Titulo")
        self.Autor = QtWidgets.QLineEdit(self.centralwidget)
        self.Autor.setGeometry(QtCore.QRect(230, 290, 561, 41))
        self.Autor.setObjectName("Autor")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(170, 230, 51, 19))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(8)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.autor = QtWidgets.QLabel(self.centralwidget)
        self.autor.setGeometry(QtCore.QRect(160, 300, 61, 20))
        self.autor.setObjectName("autor")
        self.Buscar = QtWidgets.QPushButton(self.centralwidget)
        self.Buscar.setGeometry(QtCore.QRect(300, 380, 121, 41))
        self.Buscar.setObjectName("Buscar")

        self.Buscar.clicked.connect(self.JanelaResultado)

        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(470, 380, 121, 41))
        self.cancelar.setObjectName("cancelar")
        BuscarWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BuscarWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 31))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        BuscarWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuscarWindow)
        self.statusbar.setObjectName("statusbar")
        BuscarWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCadastro.menuAction())

        self.retranslateUi(BuscarWindow)
        QtCore.QMetaObject.connectSlotsByName(BuscarWindow)

    def retranslateUi(self, BuscarWindow):
        _translate = QtCore.QCoreApplication.translate
        BuscarWindow.setWindowTitle(_translate("BuscarWindow", "BuscarWindow"))
        self.cadastro.setText(_translate("BuscarWindow", "Buscar de livro"))
        self.titulo.setText(_translate("BuscarWindow", "Titulo:"))
        self.autor.setText(_translate("BuscarWindow", "Autor(a):"))
        self.Buscar.setText(_translate("BuscarWindow", "Buscar"))
        self.cancelar.setText(_translate("BuscarWindow", "Voltar"))
        self.menuCadastro.setTitle(_translate("BuscarWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BuscarWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(BuscarWindow)
    BuscarWindow.show()
    sys.exit(app.exec_())

