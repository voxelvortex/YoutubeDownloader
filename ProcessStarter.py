import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore, QtWebKitWidgets,QtGui
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage
import os
import subprocess
import youtube_dl

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
        self.webView.installEventFilter(self)
        self.show()

    def eventFilter(self, obj, event):
        if obj == self.webView:
            if(self.webView.hasFocus() == True):
                self.getActualURL()
                self.setURLm

        return False

    def getActualURL(self):
        i = self.webView.url()
        i = str(i)
        i = i[19:]
        ilen = i.__len__()
        url = i[:ilen - 2]
        self.urlInput.setText(url)


    @pyqtSlot()
    def youtubeDownload(self):
        try:
            with youtube_dl.YoutubeDL({}) as ydl:
                login = os.getlogin()
                path = "C:/Users/"+login+"/Downloads/Youtube_Downloader"
                if not os.path.exists(path):
                    os.makedirs(path)
                os.chdir(path)
                ydl.download([str(self.urlInput.displayText())])
        except:
            msgBox = QMessageBox()
            msgBox.setText("Error:")
            msgBox.setInformativeText("An unknown error occurred. Ensure video link is correct")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec_()

    @pyqtSlot()
    def setURLm(self):
        try:
            url = self.urlInput.displayText()
            i7 = url[:7]
            i8 = url[:8]
            if (i7 == "http://" or i8 == "https://"):
                pass
            else:
                url = "http://"+url
            print(url)

            self.webView.setUrl(QUrl(url))
        except:
            pass




app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())
