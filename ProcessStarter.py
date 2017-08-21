import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore, QtWebKitWidgets,QtGui
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage
import youtube_dl
import os

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Youtube Downloader'
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


        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.urlInput.setText(_translate("MainWindow", "Enter URL here (include http://www)"))
        self.setURL.setText(_translate("MainWindow", "Go to entered URL"))
        self.downloadButton.setText(_translate("MainWindow", "Download Youtube Video"))

        self.downloadButton.clicked.connect(self.youtubeDownload)
        self.setURL.clicked.connect(self.setURLm)


        self.getActualURL()
        self.show()

    def getActualURL(self):
        i = self.webView.url()
        i = str(i)
        i = i[19:]
        ilen = i.__len__()
        i = i[:ilen - 2]
        self.urlInput.setText(i)


    def event(self, a0: QtCore.QEvent):
        self.getActualURL()


    @pyqtSlot()
    def url_changed(self, q):
        url = self.webView.setText(q.toString())
        print(url)
        self.urlInput.setText(url)

    @pyqtSlot()
    def youtubeDownload(self):
        os.system("youtube-dl -o \"~/Downloads/Youtube_Downloader/%(title)s.%(ext)s\" \"" + self.urlInput.displayText() + "\"")

    @pyqtSlot()
    def setURLm(self):
        try:
            self.webView.setUrl(QUrl(self.urlInput.displayText()))
        except:
            pass



app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
