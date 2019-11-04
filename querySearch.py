

from PyQt5 import QtCore, QtGui, QtWidgets
from cosine import main
from output import Ui_output
from PyQt5.QtWidgets import QMessageBox
from lstm import predict_relevancy

class Ui_querySearch(object):

    def openOutput(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_output()
        self.ui.setupUi(self.window,self.output_text)
        self.window.show()


    def setupUi(self, querySearch,uploadFile):

        self.path=uploadFile
        querySearch.setObjectName("querySearch")
        querySearch.resize(942, 497)
        self.horizontalLayoutWidget = QtWidgets.QWidget(querySearch)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 20, 921, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
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
        self.horizontalLayout.addWidget(self.label)
        self.Go = QtWidgets.QPushButton(querySearch)
        self.Go.setGeometry(QtCore.QRect(10, 440, 921, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Go.setFont(font)
        self.Go.setObjectName("Go")

        self.Go.clicked.connect(self.execute)


        self.groupBox = QtWidgets.QGroupBox(querySearch)
        self.groupBox.setGeometry(QtCore.QRect(760, 110, 171, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 171, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(querySearch)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 741, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.query = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.query.setFont(font)
        self.query.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.query.setObjectName("query")
        self.verticalLayout.addWidget(self.query)

        self.retranslateUi(querySearch)
        QtCore.QMetaObject.connectSlotsByName(querySearch)

    def retranslateUi(self, querySearch):
        _translate = QtCore.QCoreApplication.translate
        querySearch.setWindowTitle(_translate("querySearch", "Form"))
        self.label.setText(_translate("querySearch", "Contextual Search"))
        self.Go.setText(_translate("querySearch", "Search "))
        self.groupBox.setTitle(_translate("querySearch", "Algorithm"))
        self.radioButton_2.setText(_translate("querySearch", "Cosine Simlarity"))
        self.radioButton.setText(_translate("querySearch", "Siamese LSTM"))
        self.query.setPlaceholderText(_translate("querySearch", "Enter a keyword or query"))


    def execute(self):

        self.flag=-1
        if self.radioButton.isChecked()==True:
            self.flag=0
        elif self.radioButton_2.isChecked()==True:
            self.flag=1

        self.quest=self.query.toPlainText()
        self.forward()

    def forward(self):

        if(self.quest==""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter a query or keyword")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.flag==-1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Select an algorithm ")
            msg.setWindowTitle("Error")
            msg.exec_()

        elif self.flag==1:
            self.output_text=main(self.path,self.quest)
            self.openOutput()

        elif self.flag==0:
            self.output_text = predict_relevancy(self.path, self.quest)
            self.openOutput()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    querySearch = QtWidgets.QWidget()
    ui = Ui_querySearch()
    ui.setupUi(querySearch)
    querySearch.show()
    sys.exit(app.exec_())

