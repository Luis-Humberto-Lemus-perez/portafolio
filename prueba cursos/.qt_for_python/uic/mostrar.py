# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Documents\proyetos python\prueba cursos\mostrar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(100, 500))
        MainWindow.setMaximumSize(QtCore.QSize(700, 500))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.frame.setMinimumSize(QtCore.QSize(700, 500))
        self.frame.setMaximumSize(QtCore.QSize(700, 500))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"color: rgb(18, 82, 200);\n"
"\n"
"font: 75 12pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: white;\n"
"\n"
"\n"
"font: 75 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"    \n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"    \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_regresar = QtWidgets.QPushButton(self.frame)
        self.bt_regresar.setGeometry(QtCore.QRect(550, 450, 141, 40))
        self.bt_regresar.setMinimumSize(QtCore.QSize(100, 40))
        self.bt_regresar.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\proyetos python\\prueba cursos\\pngfind.com-back-png-1934895.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_regresar.setIcon(icon)
        self.bt_regresar.setIconSize(QtCore.QSize(32, 32))
        self.bt_regresar.setObjectName("bt_regresar")
        self.btn_mostrar = QtWidgets.QPushButton(self.frame)
        self.btn_mostrar.setGeometry(QtCore.QRect(110, 420, 141, 40))
        self.btn_mostrar.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_mostrar.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\proyetos python\\prueba cursos\\pngwing.com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mostrar.setIcon(icon1)
        self.btn_mostrar.setIconSize(QtCore.QSize(32, 32))
        self.btn_mostrar.setObjectName("btn_mostrar")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 0, 400, 35))
        self.label_8.setMinimumSize(QtCore.QSize(400, 35))
        self.label_8.setMaximumSize(QtCore.QSize(200, 30))
        self.label_8.setObjectName("label_8")
        self.tble = QtWidgets.QTableWidget(self.frame)
        self.tble.setGeometry(QtCore.QRect(40, 50, 621, 361))
        self.tble.setStyleSheet("")
        self.tble.setObjectName("tble")
        self.tble.setColumnCount(7)
        self.tble.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tble.setHorizontalHeaderItem(6, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agregar Cursos"))
        self.bt_regresar.setText(_translate("MainWindow", "Regresar"))
        self.btn_mostrar.setText(_translate("MainWindow", "Mostrar"))
        self.label_8.setText(_translate("MainWindow", "Mostrar Cursos de la Lista"))
        item = self.tble.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tble.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre del Curso"))
        item = self.tble.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Pre requisito"))
        item = self.tble.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Opcional"))
        item = self.tble.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Semestre"))
        item = self.tble.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Creditos"))
        item = self.tble.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Estado"))