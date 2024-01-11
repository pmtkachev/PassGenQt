import sys

from PyQt5 import QtWidgets

from main_window import Ui_MainWindow
from styles import style


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])

app.setStyleSheet(style)
application = MainWindow()
application.show()

sys.exit(app.exec())
