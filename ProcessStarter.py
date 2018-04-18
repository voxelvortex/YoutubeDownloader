from __future__ import unicode_literals
import sys
import subprocess
import os
from pathlib import Path
import pip

path = os.getcwd()




mf = Path(path+"/first.txt")
if not (mf.is_file()):
    open(path+"/first.txt", 'w').close()
    pip.main(['install', 'youtube-dl'])
    pip.main(['install', 'PyQt5'])
    pip.main(['install','avprobe'])

import MainWindow
from MainWindow import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
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
        self.gridLayout.addWidget(self.webView, 1, 0, 1, 0)
        self.webView.installEventFilter(self)
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        self.getActualURL()
        self.downloadVideoButton.clicked.connect(self.downloadVideo)
        self.downloadMp3Button.clicked.connect(self.downloadMp3)
        self.setURL.clicked.connect(self.setURLm)
        self.getActualURL()

    def getActualURL(self):
        i = self.webView.url()
        i = str(i)
        i = i[19:]
        ilen = i.__len__()
        url = i[:ilen - 2]
        print(url)
        self.urlInput.setText(url)

    def youtubeDownload(self,type):
        self.getActualURL()
        if type==1:
            ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],}
        else:
            ydl_opts = {}
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                msgBox = QMessageBox()
                ydl.download([str(self.urlInput.displayText())])
                msgBox.setWindowTitle('Finished')
                msgBox.setText("Your video has finished downloading.\nIt is available at "+path)
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.setDefaultButton(QMessageBox.Ok)
                msgBox.exec_()
        except:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("An error occurred. Ensure video link is correct")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            msgBox.exec_()

    @pyqtSlot()
    def downloadVideo(self):
        self.youtubeDownload(0)

    @pyqtSlot()
    def downloadMp3(self):
        self.youtubeDownload(1)

    @pyqtSlot()
    def setURLm(self):
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

        @pyqtSlot()
        def eventFilter(self, obj, event):
            print("T")

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
l.setWindowIcon(QIcon(path+"\\YTDL.png"))

path = path + "\\Downloads"
print(path)
if not os.path.exists(path):
    os.makedirs(path)
os.chdir(path)
sys.exit(app.exec_())
