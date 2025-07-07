import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QComboBox, QPushButton,
                             QLabel, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from FancyContainers import FancyContainer1, FancyContainer2
from CharacterInformation import lee_hyunsung, kim_namwoon
from CharacterWindow import CharacterWindow

class CharacterSelector(FancyContainer1):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Select Character')
        self.setFixedSize(280, 140)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)

        str_section = "CHARACTER SELECTOR"

        # Add the characters
        self.characters = {
            "Lee Hyunsung": lee_hyunsung,
            "Kim Namwoon": kim_namwoon
        }

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)



        ################ TOP SECTION ######################
        # Section
        top_container = FancyContainer2()
        top_container.setObjectName("TopContainer")
        top_layout = QHBoxLayout(top_container)
        main_layout.addWidget(top_container)

        self.label_title = QLabel("< " + str_section + " >", self)
        self.label_title.setObjectName("TitleSection")
        top_layout.addWidget(self.label_title)
        top_layout.addStretch()

        # Buttons
        self.btn_min = QPushButton('\u2013')
        self.btn_close = QPushButton('\u2715')

        for btn in [self.btn_min, self.btn_close]:
            btn.setFixedSize(25, 25)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
            top_layout.addWidget(btn)

            # Connect the buttons
        self.btn_min.clicked.connect(self.showMinimized)
        self.btn_close.clicked.connect(self.close)



        ################ BODY SECTION #####################
        self.combo = QComboBox()
        self.combo.addItems(self.characters.keys())
        main_layout.addWidget(self.combo)

        self.btn_open = QPushButton('Open Character Window')
        self.btn_open.clicked.connect(self.open_character)
        main_layout.addWidget(self.btn_open)

    def open_character(self):
        name = self.combo.currentText()
        info = self.characters[name]
        try:
            self.window = CharacterWindow(info)
            self.window.show()
        except Exception as e:
            import traceback
            print("Ocurrió un error al abrir CharacterWindow:")
            traceback.print_exc()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.label_title.underMouse():
            self._startPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._startPos:
            self.move(event.globalPos() - self._startPos)
            event.accept()
    def mouseReleaseEvent(self, event):
        self._startPos = None

if __name__ == '__main__':
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), 'style.qss')
    try:
        with open(qss_path, 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("⚠️ The file 'style.qss' was not found. Styles not applied.")
    selector = CharacterSelector()
    selector.show()
    sys.exit(app.exec())
