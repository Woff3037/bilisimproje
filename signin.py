# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 200)
        self.verticalLayoutWidget = QtWidgets.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.kayitmaili = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.kayitmaili.setText("")
        self.kayitmaili.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.kayitmaili)
        self.kayitsifresi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.kayitsifresi.setText("")
        self.kayitsifresi.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.kayitsifresi.setClearButtonEnabled(False)
        self.kayitsifresi.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.kayitsifresi)
        self.kayitol = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.kayitol.setObjectName("PushButton")
        self.verticalLayout.addWidget(self.kayitol)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Sign Up"))
        self.kayitmaili.setPlaceholderText(_translate("Widget", "Email"))
        self.kayitsifresi.setPlaceholderText(_translate("Widget", "Password"))
        self.kayitol.setText(_translate("Widget", "Sign Up"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec())