from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

import os
import sys


# using the resource_path function to ensure the icon path is correctly located in both the development and bundled
# environments.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet(
            "QFrame { background-color: rgb(211, 229, 245); color: rgb(43, 17, 242); border-radius: 10px; }")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 40, 661, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: black;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(0, 110, 661, 31))
        font.setPointSize(13)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(43, 17, 242);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 290, 561, 23))
        self.progressBar.setStyleSheet("""
            QProgressBar {
                background-color: rgb(6, 169, 177);
                color: white;
                border-style: none;
                border-radius: 10px;
                text-align: center;
            }
            QProgressBar::chunk {
                border-radius: 10px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgb(50, 223, 111, 119), stop:1 rgb(35, 81, 184, 226));
            }
        """)
        self.progressBar.setValue(24)
        self.progressBar.setObjectName("progressBar")
        self.labelimg = QLabel(self.dropShadowFrame)
        self.labelimg.setText("")

        # Use the resource_path function to load the logo
        logo_path = resource_path("JPG_PNG IMAGES/al-codon-high-resolution-logo-transparent.png")
        pixmap = QtGui.QPixmap(logo_path)
        scaled_pixmap = pixmap.scaled(99, 99, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.labelimg.setPixmap(scaled_pixmap)

        self.labelimg.setGeometry(QRect(278, 160, 99, 99))
        self.labelimg.setAlignment(Qt.AlignCenter)

        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName("label_credits")
        # self.label_credits.setGeometry(QRect(270, 330, 621, 23))
        self.label_credits.setGeometry(QRect(155, 330, 621, 23))

        font3 = QFont()
        font3.setFamily("Segoe UI")
        font3.setPointSize(9)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet("color: #4dc477;")
        self.label_credits.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label_credits.setText(
            '<strong>Created by: <a href="mailto:houssembenkhalfallah@gmail.com">Houssem BEN KHALFALLAH</a> © 2024</strong>')
        self.label_credits.setTextFormat(QtCore.Qt.RichText)
        self.label_credits.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_credits.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate("SplashScreen", "AL-CODON Counter"))
        self.label_description.setText(
            _translate("SplashScreen", "<strong>WELCOME</strong> to CODON COUNTER ASSISTANT"))
