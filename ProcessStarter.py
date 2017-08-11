import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore, QtWebKitWidgets,QtGui

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Youtube Downloader'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setObjectName("MainWindow")
        self.resize(824, 696)
        self.setMinimumSize(QtCore.QSize(250, 150))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QtCore.QSize(1218, 836))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.urlInput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.urlInput.setFont(font)
        self.urlInput.setClearButtonEnabled(False)
        self.urlInput.setObjectName("urlInput")
        self.verticalLayout.addWidget(self.urlInput)
        self.setURL = QtWidgets.QPushButton(self.centralwidget)
        self.setURL.setObjectName("setURL")
        self.verticalLayout.addWidget(self.setURL)
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("https://www.youtube.com/"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.verticalLayout.addWidget(self.downloadButton)
        #self.setCentralWidget(self.centralwidget)
        #self.menubar = QtWidgets.QMenuBar(self)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        #self.menubar.setObjectName("menubar")
        #self.setMenuBar(self.menubar)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.urlInput.setText(_translate("MainWindow", "Enter URL here (include http://www)"))
        self.setURL.setText(_translate("MainWindow", "Go to entered URL"))
        self.downloadButton.setText(_translate("MainWindow", "Download Youtube Video"))

        #button = QPushButton('PyQt5 button', self)
        #button.setToolTip('This is an example button')
        #button.move(100,70)
        #button.clicked.connect(self.on_click)

        self.downloadButton.clicked.connect(self.youtubeDownload)
        #self.setURL.clicked.connect(self.setURL)
        i = (self.webView.url())
        self.urlInput.setText(str(i))
        self.webView.setUrl(i)
        print(i)

        self.show()

    @pyqtSlot()
    def youtubeDownload(self):
        print('PyQt5 button click')

    @pyqtSlot()
    def setURL(self):
        print("setUrl")

    def event(self, a0: QtCore.QEvent):
        print("url")



app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
