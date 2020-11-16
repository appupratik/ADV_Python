from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(407, 203)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 70, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.textEditPratik = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditPratik.setGeometry(QtCore.QRect(40, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditPratik.setFont(font)
        self.textEditPratik.setObjectName("textEditPratik")
        self.lineEditPratik = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditPratik.setGeometry(QtCore.QRect(40, 100, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditPratik.setFont(font)
        self.lineEditPratik.setObjectName("lineEditPratik")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pratik Bhatt"))
        self.checkBox.setText(_translate("MainWindow", "Click to Paste "))
        self.checkBox.stateChanged.connect(self.pratik)
        
    def pratik(self):
        data = self. textEditPratik.toPlainText()
        self.lineEditPratik.setText(str(data))
        self.checkBox.setText("Done")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
