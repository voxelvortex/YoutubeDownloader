# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 728)
        MainWindow.setMinimumSize(QtCore.QSize(250, 150))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 835))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMaximumSize(QtCore.QSize(1218, 836))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setObjectName("downloadButton")
        self.gridLayout.addWidget(self.downloadButton, 2, 0, 1, 2)
        self.urlInput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.urlInput.setFont(font)
        self.urlInput.setClearButtonEnabled(False)
        self.urlInput.setObjectName("urlInput")
        self.gridLayout.addWidget(self.urlInput, 0, 0, 1, 1)
        self.setURL = QtWidgets.QPushButton(self.centralwidget)
        self.setURL.setObjectName("setURL")
        self.gridLayout.addWidget(self.setURL, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Downloader"))
        self.downloadButton.setText(_translate("MainWindow", "Download Youtube Video"))
        self.urlInput.setText(_translate("MainWindow", "Enter URL here (include http://www)"))
        self.setURL.setText(_translate("MainWindow", "Go to entered URL"))

