# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CadastroWindow(object):


    def _on_button_clicked(self):
        titulo= self.titulo.text()
        Autor = self.Autor.text()
        Ano = self.Ano.text()

    def setupUi(self, CadastroWindow):
        CadastroWindow.setObjectName("CadastroWindow")
        CadastroWindow.resize(886, 660)
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        CadastroWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CadastroWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cadastro = QtWidgets.QLabel(self.centralwidget)
        self.cadastro.setGeometry(QtCore.QRect(30, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cadastro.setFont(font)
        self.cadastro.setObjectName("cadastro")
        self.Titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(220, 120, 561, 41))
        self.Titulo.setObjectName("Titulo")
        self.Autor = QtWidgets.QLineEdit(self.centralwidget)
        self.Autor.setGeometry(QtCore.QRect(220, 180, 561, 41))
        self.Autor.setObjectName("Autor")
        self.Ano = QtWidgets.QLineEdit(self.centralwidget)
        self.Ano.setGeometry(QtCore.QRect(220, 240, 561, 41))
        self.Ano.setObjectName("Ano")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(170, 130, 51, 19))
        font = QtGui.QFont()
        font.setFamily("Miriam CLM")
        font.setPointSize(8)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.autor = QtWidgets.QLabel(self.centralwidget)
        self.autor.setGeometry(QtCore.QRect(160, 190, 61, 20))
        self.autor.setObjectName("autor")
        self.ano = QtWidgets.QLabel(self.centralwidget)
        self.ano.setGeometry(QtCore.QRect(180, 250, 41, 19))
        self.ano.setObjectName("ano")
        self.pag = QtWidgets.QLabel(self.centralwidget)
        self.pag.setGeometry(QtCore.QRect(130, 300, 81, 20))
        self.pag.setObjectName("pag")
        self.paginas = QtWidgets.QSpinBox(self.centralwidget)
        self.paginas.setGeometry(QtCore.QRect(220, 300, 51, 31))
        self.paginas.setMaximum(500000)
        self.paginas.setObjectName("paginas")
        self.salvar = QtWidgets.QPushButton(self.centralwidget)
        self.salvar.setGeometry(QtCore.QRect(300, 400, 121, 41))
        self.salvar.setObjectName("salvar")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(470, 400, 121, 41))
        self.cancelar.setObjectName("cancelar")
        CadastroWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CadastroWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 886, 31))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        CadastroWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CadastroWindow)
        self.statusbar.setObjectName("statusbar")
        CadastroWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCadastro.menuAction())

        self.retranslateUi(CadastroWindow)
        QtCore.QMetaObject.connectSlotsByName(CadastroWindow)

    def retranslateUi(self, CadastroWindow):
        _translate = QtCore.QCoreApplication.translate
        CadastroWindow.setWindowTitle(_translate("CadastroWindow", "CadastroWindow"))
        self.cadastro.setText(_translate("CadastroWindow", "Cadastro de livro"))
        self.titulo.setText(_translate("CadastroWindow", "Titulo:"))
        self.autor.setText(_translate("CadastroWindow", "Autor(a):"))
        self.ano.setText(_translate("CadastroWindow", "Ano:"))
        self.pag.setText(_translate("CadastroWindow", "Nº páginas:"))
        self.salvar.setText(_translate("CadastroWindow", "Salvar"))
        self.cancelar.setText(_translate("CadastroWindow", "Cancelar"))
        self.menuCadastro.setTitle(_translate("CadastroWindow", "Cadastro"))


if __name__ == "__cadastro__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadastroWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(CadastroWindow)
    CadastroWindow.show()
    sys.exit(app.exec_())

