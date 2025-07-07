import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from FancyContainers import FancyContainer1, FancyContainer2
from CharacterInformation import lee_hyunsung, kim_namwoon

# addStretch() adds an expandable space that 'pushes' the widgets that come after it to the opposite side.

class CharacterWindow(FancyContainer1):
    def __init__(self, character_info):
        super().__init__()
        self.character = character_info
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Character Window")
        self.setGeometry(900, 10, 350, 600) # (x, y, width, height)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._startPos = None

        # Layouts
        self.setObjectName("MainWindow")
        main_layout = QVBoxLayout(self)



        ################ CHARACTER INFO ###################
        str_section = "CHARACTER INFORMATION"
        str_name = self.character.name
        str_age = self.character.age
        str_sponsor = self.character.sponsor
        str_exclu_at = self.character.exclu_at
        str_exclu_at_grade = self.character.exclu_at_grade
        skills = self.character.skills
        stigmas = self.character.stigmas
        stats = self.character.stats
        str_evaluation = self.character.evaluation



        ################ TOP SECTION ######################
        # Top (title n buttons)
        top_container = FancyContainer2()
        top_container.setObjectName("TopContainer")
        top_layout = QHBoxLayout(top_container)
        main_layout.addWidget(top_container)

        # Add labels
        self.label_title = QLabel("< " + str_section + " >", self)
        self.label_title.setObjectName("TitleSection")
        top_layout.addWidget(self.label_title)
        top_layout.addStretch()

        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(0) # Quit space between btns

            # Add buttons
        self.btn_min = QPushButton('\u2013', self)
        self.btn_restore = QPushButton('\u2750', self)
        self.btn_close = QPushButton('\u2715', self)

        for btn in [self.btn_min, self.btn_restore, self.btn_close]:
            btn.setFixedSize(25, 25) # Size the buttons
            btn.setCursor(QCursor(Qt.PointingHandCursor)) # Set cursor
            btn_layout.addWidget(btn) # Add to layer

            # Connect the buttons
        self.btn_min.clicked.connect(self.on_button_min_click)
        self.btn_restore.clicked.connect(self.on_button_restore_click)
        self.btn_close.clicked.connect(self.on_button_close_click)

        top_layout.addLayout(btn_layout)



        ################ BODY SECTION #####################
        # Body (information)
        body_container = QWidget()
        body_container.setObjectName("BodyContainer")
        body_layout = QVBoxLayout(body_container)
        main_layout.addWidget(body_container)
        main_layout.addStretch()
        # Add information in labels
        info1_layout = QVBoxLayout()
        self.label_name = QLabel("NAME: " + str_name, self)
        self.label_age = QLabel("AGE: " + str_age, self)
        self.label_sponsor = QLabel("CONSTELLATION SPONSOR: " + str_sponsor, self)
        info1_layout.addWidget(self.label_name)
        info1_layout.addWidget(self.label_age)
        info1_layout.addWidget(self.label_sponsor)

        info2_layout = QVBoxLayout()
        self.label_exclu_at = QLabel("EXCLUSIVE ATTRIBUTE: " + str_exclu_at + " ("+ str_exclu_at_grade + ")")
        self.label_exclu_at.setWordWrap(True)
        self.label_exclu_at.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        info2_layout.addWidget(self.label_exclu_at)

        info3_layout = QHBoxLayout()
        self.label_exclu_skills = QLabel("EXCLUSIVE SKILLS: ")
        text_skills = ', '.join([f"[{name}\u00A0LV.{lvl}]" for name, lvl in skills])
        self.label_all_skill = QLabel(text_skills)
        self.label_all_skill.setWordWrap(True)
        # self.label_all_skill.setFixedWidth(200)
        self.label_all_skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        info3_layout.setSpacing(0)
        info3_layout.addWidget(self.label_exclu_skills, alignment=Qt.AlignTop)
        info3_layout.addWidget(self.label_all_skill)
        info3_layout.addStretch()

        info4_layout = QHBoxLayout()
        self.label_stigma = QLabel("STIGMA: ")
        text_stigmas = ', '.join([f"[{name}\u00A0LV.{lvl}]" for name, lvl in stigmas])
        self.label_all_stigmas = QLabel(text_stigmas)
        self.label_all_stigmas.setWordWrap(True)
        self.label_all_stigmas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        info4_layout.setSpacing(0)
        info4_layout.addWidget(self.label_stigma, alignment=Qt.AlignTop)
        info4_layout.addWidget(self.label_all_stigmas)
        info4_layout.addStretch()

        info5_layout = QHBoxLayout()
        self.label_stats = QLabel("OVERALL STATS: ")
        text_stats = ', '.join([f"[{name}\u00A0LV.{lvl}]" for name, lvl in stats])
        self.label_all_stats = QLabel(text_stats)
        self.label_all_stats.setWordWrap(True)
        self.label_all_stats.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        info5_layout.setSpacing(0)
        info5_layout.addWidget(self.label_stats, alignment=Qt.AlignTop)
        info5_layout.addWidget(self.label_all_stats)
        info5_layout.addStretch()

        info6_layout = QHBoxLayout()
        self.label_evaluation = QLabel("OVERALL EVALUATON: \n" + str_evaluation)
        self.label_evaluation.setWordWrap(True)
        info6_layout.addWidget(self.label_evaluation)

        body_layout.addLayout(info1_layout)
        body_layout.addLayout(info2_layout)
        body_layout.addLayout(info3_layout)
        body_layout.addLayout(info4_layout)
        body_layout.addLayout(info5_layout)
        body_layout.addLayout(info6_layout)
        
        body_container.setLayout(body_layout)

    def on_button_min_click(self):
        self.showMinimized()
    def on_button_restore_click(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    def on_button_close_click(self):
        self.close()

    def mousePressEvent(self, event):
        # Only start movement if you click on the QLabel TitleSection
        if event.button() == Qt.LeftButton and self.label_title.underMouse():
            self._startPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self._startPos:
            self.move(event.globalPos() - self._startPos)
            event.accept()
    def mouseReleaseEvent(self, event):
        self._startPos = None


if __name__ == "__main__":
    app = QApplication(sys.argv) # Create the application instance

    # Get a safe absolute path to the .qss file
    qss_path = os.path.join(os.path.dirname(__file__), 'style.qss')

    try:
        with open(qss_path, 'r') as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError:
        print("⚠️ The file 'style.qss' was not found. Styles not applied.")

    window = CharacterWindow() # Create the window
    window.show()
    sys.exit(app.exec()) # Start the event loop

# Modificaciones:
#     hacer que los labels se agrupen, ver en la imagen de referencia
#     hacer que los bordes no sean cuadrados