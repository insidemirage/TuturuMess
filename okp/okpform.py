
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

import os
class Ui_Form(object):
    def setupUi(self, Form):
        self.resources = os.path.dirname(__file__).replace('\\', "/")
        kpath = self.resources+"/src/kwork.png"
        logmaskfolder = self.resources+"/src/logmask.png"

        Form.setObjectName("Form")
        Form.resize(251, 250)
        Form.setStyleSheet("background-color:white; border-radius:10px")
        logmask = QPixmap(logmaskfolder)
        Form.setMask(logmask.mask())
        Form.setWindowFlags(Qt.FramelessWindowHint)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(54, 55))
        self.label.setMaximumSize(QtCore.QSize(54, 55))
        self.label.setStyleSheet("border-image:url({0})  stretch stretch;\n".format(kpath))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 25))
        self.label_2.setStyleSheet("margin-left:10px;\n"
"margin-top:10px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("width:181px;\n"
"height:32px;\n"
"margin-right:10px;\n"
"margin-left:10px;\n"
"border-radius:10px;\n"
"border:1px solid #877B79;\n"
"padding-left:10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(60, 25))
        self.label_3.setStyleSheet("margin-left:10px;\n"
"margin-top:10px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("width:181px;\n"
"height:32px;\n"
"margin-right:10px;\n"
"margin-left:10px;\n"
"border-radius:10px;\n"
"border:1px solid #877B79;\n"
"padding-left:10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("margin-top: 10px;\n"
"border:1px solid #877B79;\n"
"background-color:white;\n"
"border-radius:10px;\n"
"height:40px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"font: 16pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(50, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Логин:"))
        self.label_3.setText(_translate("Form", "Пароль:"))
        self.pushButton.setText(_translate("Form", "Вход"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

