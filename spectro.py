from PyQt5 import QtWidgets 
from PyQt5 import QtCore 
from PyQt5 import QtGui
from gui import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
 
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
