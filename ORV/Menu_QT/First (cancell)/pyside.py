import sys
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('mainwindow.ui', self)
        self.setMenuBarHeight()

    def setMenuBarHeight(self):
        menu_bar = self.findChild(QtWidgets.QHBoxLayout, 'MenuBar')
        menu_bar_widget = menu_bar.itemAt(0).widget()
        menu_bar_widget.setFixedHeight(189)  # 5 cm converted to pixels

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
