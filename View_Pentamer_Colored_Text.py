from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys


# using the resource_path function to ensure the icon path is correctly located in both the development and bundled
# environments.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("MainWindow_2")
        MainWindow_2.resize(560, 490)
        # Use the resource_path function to load the logo
        logo_path_2 = resource_path("JPG_PNG IMAGES/logo.png")
        MainWindow_2.setWindowIcon(QtGui.QIcon(logo_path_2))
        self.centralwidget = QtWidgets.QWidget(MainWindow_2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Selected_pentamer = QtWidgets.QLabel(self.centralwidget)
        self.label_Selected_pentamer.setGeometry(QtCore.QRect(20, 20, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Selected_pentamer.setFont(font)
        self.label_Selected_pentamer.setTextFormat(QtCore.Qt.RichText)
        self.label_Selected_pentamer.setObjectName("label_Selected_pentamer")
        self.textEdit_Selected_Pentamer_Occurence = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Selected_Pentamer_Occurence.setGeometry(QtCore.QRect(20, 80, 521, 361))
        self.textEdit_Selected_Pentamer_Occurence.setObjectName("textEdit_Selected_Pentamer_Occurence")
        MainWindow_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_2)
        self.statusbar.setObjectName("statusbar")
        MainWindow_2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)

    def retranslateUi(self, MainWindow_2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_2.setWindowTitle(_translate("MainWindow_2", "View Selected Pentamer Occurence"))
        self.label_Selected_pentamer.setText(_translate("MainWindow_2", "Occurence Of The Selected Pentamer "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_2()
    ui.setupUi(MainWindow_2)
    MainWindow_2.show()
    sys.exit(app.exec_())
