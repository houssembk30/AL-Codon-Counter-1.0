from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from ui_splash_screen import Ui_SplashScreen


class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)

        ## CHANGE DESCRIPTION
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>Loading</strong>  "
                                                                                 "interfaces..."))

        ## SHOW ==> MAIN WINDOW
        self.show()
        self.counter = 0

    def progress(self):
        self.counter += 1
        self.ui.progressBar.setValue(self.counter)

        if self.counter >= 100:
            self.timer.stop()
            from interface_AL_Counter import ALCodonCounterMainWindow  # Moved import here to avoid circular import
            self.main = ALCodonCounterMainWindow()
            self.main.showMaximized()
            self.close()
