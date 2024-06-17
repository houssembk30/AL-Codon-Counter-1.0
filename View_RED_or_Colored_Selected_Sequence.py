from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys


# using the resource_path function to ensure the icon path is correctly located in both the development and bundled
# environments.
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow_3):
        MainWindow_3.setObjectName("MainWindow_3")
        MainWindow_3.resize(560, 490)
        # Use the resource_path function to load the logo
        logo_path_3 = resource_path("JPG_PNG IMAGES/logo.png")
        MainWindow_3.setWindowIcon(QtGui.QIcon(logo_path_3))
        self.centralwidget = QtWidgets.QWidget(MainWindow_3)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Selected_pentamer = QtWidgets.QLabel(self.centralwidget)
        self.label_Selected_pentamer.setGeometry(QtCore.QRect(20, 20, 231, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_Selected_pentamer.setFont(font)
        self.label_Selected_pentamer.setTextFormat(QtCore.Qt.RichText)
        self.label_Selected_pentamer.setObjectName("label_Selected_Sequence")
        self.textEdit_Selected_Sequence = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Selected_Sequence.setGeometry(QtCore.QRect(20, 80, 521, 361))
        self.textEdit_Selected_Sequence.setObjectName("textEdit_Selected_Sequence")
        MainWindow_3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_3)
        self.statusbar.setObjectName("statusbar")
        MainWindow_3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_3)

    def retranslateUi(self, MainWindow_3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_3.setWindowTitle(_translate("MainWindow_3", "View Selected Sequence"))
        self.label_Selected_pentamer.setText(_translate("MainWindow_3", "Red / Colored  Selected Sequence "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_3()
    ui.setupUi(MainWindow_3)
    MainWindow_3.show()
    sys.exit(app.exec_())
