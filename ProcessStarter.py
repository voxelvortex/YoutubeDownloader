import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore, QtGui, QtTest
from PyQt5 import QtWebEngine,QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os, subprocess, youtube_dl, MainWindow
from MainWindow import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.webView.load(self.webView,("http://www.Youtube.com"))
        self.webView.setEnabled(True)
        self.webView.setObjectName("webView")
        self.webView.setBaseSize(30, 30)


        ui.downloadButton.setEnabled(False)
        ui.setURL.setEnabled(False)
        self.downloadButton.clicked.connect(self.youtubeDownload)
        self.setURL.clicked.connect(self.setURLm)
        self.getActualURL()
        self.webView.installEventFilter(self)

    def event(self,obj):
        if obj == self.webView:
            if(self.webView.hasFocus() == True):
                self.getActualURL()
                self.setURLm

        return False

    def getActualURL(self):
        print("getactualurl")
        i = self.webView.url()
        i = str(i)
        i = i[19:]
        ilen = i.__len__()
        url = i[:ilen - 2]
        self.urlInput.setText(url)


    @pyqtSlot()
    def youtubeDownload(self):
        print("ytdownload")
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
        print("seturlm")
        try:
            url = self.urlInput.displayText()
            i7 = url[:7]
            i8 = url[:8]
            if (i7 == "http://" or i8 == "https://"):
                pass
            else:
                url = "http://"+url
            print(url)

            self.webView.load(QUrl(url))
        except:
            pass

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
