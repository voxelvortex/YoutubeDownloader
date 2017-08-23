import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtTest
from PyQt5 import *
from PyQt5 import QtWidgets, QtCore, QtWebKitWidgets,QtGui,QtWebKit,QtWebSockets,QtWebChannel
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage
import os
import subprocess
import youtube_dl
import MainWindow
from MainWindow import *

class App(QWidget,Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.ui = Ui_MainWindow
        self.ui.setupUi(self, self)
        QtWebKit.QWebSettings.globalSettings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
        self.show()

        self.downloadButton.clicked.connect(self.youtubeDownload)
        self.setURL.clicked.connect(self.setURLm)
        self.getActualURL()
        self.webView.installEventFilter(self)

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
