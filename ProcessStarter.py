import sys
import subprocess
import os
from pathlib import Path
import pip

path = str(os.path.dirname(os.path.realpath(__file__)))
pyLoc = sys.executable
pyLoc = pyLoc[:-10] + "Scripts"
print(pyLoc,path)

mf = Path(path+"/first.txt")
if not mf.is_file():
    open(path+"/first.txt", 'w').close()
    pip.main(['install', 'youtube-dl'])
    pip.main(['install', 'PyQt5'])

import MainWindow
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore, QtGui, QtTest, QtWebEngine,QtWebEngineWidgets, QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineView
import youtube_dl

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
        self.webView.installEventFilter(self)


        self.getActualURL()
        self.downloadButton.clicked.connect(self.youtubeDownload)
        self.setURL.clicked.connect(self.setURLm)
        self.getActualURL()


    def getActualURL(self):
        print("getactualurl")
        i = self.webView.url()
        print(i)
        i = str(i)
        i = i[19:]
        ilen = i.__len__()
        url = i[:ilen - 2]
        print(url)
        self.urlInput.setText(url)

    @pyqtSlot()
    def youtubeDownload(self):
        self.getActualURL()
        print("ytdownload")
        try:
            with youtube_dl.YoutubeDL({}) as ydl:
                dirname = os.path.split(os.path.abspath(__file__))
                path = dirname[0] + "\\Downloads"
                print("script: __file__ is", path)
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
            shortcut = False
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

        def eventFilter(self, obj, event):

            #if(obj == self.webView):
            self.getActualURL()
            if event.type() == QtCore.QEvent.MouseButtonPress:
                print("t")
            #in (QtCore.QEvent.MouseButtonPress,QtCore.QEvent.MouseButtonDblClick):
            if event.button() == QtCore.Qt.LeftButton:
                print("left")
            if event.button() == QtCore.Qt.ExtraButton1:
                self.webView.back()
            if event.button() == QtCore.Qt.ExtraButton2:
                    self.webView.forward()

            return QtGui.QWidget.eventFilter(self, obj, event)

app = QApplication(sys.argv)
l = App()
l.show()
l.setWindowIcon(QIcon(path+"/YTDL.png"))
sys.exit(app.exec_())
