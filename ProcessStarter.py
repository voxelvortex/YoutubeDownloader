import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore, QtGui, QtTest
from PyQt5 import QtWebEngine,QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os, subprocess, youtube_dl, MainWindow
from MainWindow import *

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setUpStuff()

    def setUpStuff(self):

        self.webView = QWebEngineView()
        self.webView.load(QUrl('http://youtube.com'))
        self.webView.setBaseSize(500,500)
        self.webView.setVisible(True)
        self.gridLayout.addWidget(self.webView, 1, 0, 1, 2)
        #self.webView.installEventFilter(self)


        self.getActualURL()
        self.downloadButton.clicked.connect(self.youtubeDownload)
        self.setURL.clicked.connect(self.setURLm)
        self.getActualURL()


    def getActualURL(self):
        print("getactualurl")
        i = self.webView.url()
        i = str(i)
        i = i[19:]
        ilen = i.__len__()
        url = i[:ilen - 2]
        print(url)
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
    '''def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            print("t")'''

    def eventFilter(self, obj, event):
        print("T")
        if(obj == self.webView):
            print("t")



app = QApplication(sys.argv)
l = App()
l.show()
path = str(os.path.dirname(os.path.realpath(__file__)))
l.setWindowIcon(QIcon(path+"/YTDL.png"))

sys.exit(app.exec_())
