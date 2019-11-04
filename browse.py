from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import easygui
from querySearch import Ui_querySearch


class Ui_MainWindow(object):

    def openQuerySearch(self):
        if (self.uploadFile.text() == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Blank directory ")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            self.window=QtWidgets.QMainWindow()
            self.ui=Ui_querySearch()
            self.ui.setupUi(self.window,self.uploadFile.text())
            self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 19, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.uploadFile = QtWidgets.QLineEdit(self.centralwidget)
        self.uploadFile.setGeometry(QtCore.QRect(20, 121, 641, 31))
        self.uploadFile.setObjectName("uploadFile")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(670, 120, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 741, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upload = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setObjectName("upload")
        self.verticalLayout.addWidget(self.upload)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browse.clicked.connect(self.openFile)
        self.upload.clicked.connect(self.openQuerySearch)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Contextual Search"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.upload.setText(_translate("MainWindow", "Upload"))

    def openFile(self):

        text = easygui.diropenbox()
        self.uploadFile.setText(text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



