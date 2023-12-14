import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize

import Funciones
from Pokedex import Pokedex

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super(MenuPrincipal, self).__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Menu Principal")
        self.setGeometry(100, 100, 700, 500) # (x, y, ancho, alto)
        self.pokedex_window = None # Variable de instancia para almacenar la ventana de la Pokédex

        #  _______________________________________________________________________________________
        # |                  Creación de layouts contenedores                                     |
        # |_______________________________________________________________________________________|
        layout_principal = QVBoxLayout()

        layout_titulo = QHBoxLayout()
        titulo = Funciones.Transform_IMG('PokemonCSV/images/titulo_pokemenu.png')
        layout_titulo.addWidget(titulo)
        layout_cuerpo1 = QHBoxLayout()
        layout_cuerpo2 = QHBoxLayout()

        #  _______________________________________________________________________________________
        # |                  Contenido de layout_cuerpo1 (pokedex y movimientos)                  |
        # |_______________________________________________________________________________________|
        layout_cuerpo_izq1 = QVBoxLayout()
        # imgPokedex = Funciones.Transform_IMG('PokemonCSV/images/pokedex.png', 100, 100)
        btnPokedex = QPushButton(
            icon=QIcon('PokemonCSV/icons/pokedex.ico'),
            text='Pokedex', parent=self
        )
        btnPokedex.setFixedSize(150, 50)
        btnPokedex.clicked.connect(self.press_btnPokedex)
        # layout_cuerpo_izq1.addWidget(imgPokedex)
        layout_cuerpo_izq1.addWidget(btnPokedex)

        layout_cuerpo_der1 = QVBoxLayout()
        # imgTipo = Funciones.Transform_IMG('PokemonCSV/images/tablatipo.png', 100, 100)
        btnTipo = QPushButton(
            icon=QIcon('PokemonCSV/icons/mensajes.ico'),
            text='Movimientos', parent=self
        )
        btnTipo.setFixedSize(150, 50)
        btnTipo.clicked.connect(press_btnTipo)
        # layout_cuerpo_der1.addWidget(imgTipo)
        layout_cuerpo_der1.addWidget(btnTipo)

        #  _______________________________________________________________________________________
        # |                  Contenido de layout_cuerpo2 (rivales y combate)                      |
        # |_______________________________________________________________________________________|
        layout_cuerpo_izq2 = QVBoxLayout()
        # imgRivales = Funciones.Transform_IMG('PokemonCSV/images/rivales.png', 100, 100)
        btnRivales = QPushButton(
            icon=QIcon('PokemonCSV/icons/rivales.ico'),
            text='Rivales', parent=self
        )
        btnRivales.setFixedSize(150, 50)
        btnRivales.clicked.connect(press_btnRivales)
        # layout_cuerpo_izq2.addWidget(imgRivales)
        layout_cuerpo_izq2.addWidget(btnRivales)

        layout_cuerpo_der2 = QVBoxLayout()
        # imgCombate = Funciones.Transform_IMG('PokemonCSV/images/combate.png', 100, 100)
        btnCombate = QPushButton(
            icon=QIcon('PokemonCSV/icons/combate.ico'),
            text='Combate', parent=self
        )
        btnCombate.setFixedSize(150, 50)
        btnCombate.clicked.connect(press_btnCombate)
        # layout_cuerpo_der2.addWidget(imgCombate)
        layout_cuerpo_der2.addWidget(btnCombate)

        #  _______________________________________________________________________________________
        # |                  Agrega los layouts (der-izq) 1, 2 al layout cuerpo 1, 2              |
        # |_______________________________________________________________________________________|
        layout_cuerpo1.addLayout(layout_cuerpo_izq1)
        layout_cuerpo1.addLayout(layout_cuerpo_der1)
        layout_cuerpo2.addLayout(layout_cuerpo_izq2)
        layout_cuerpo2.addLayout(layout_cuerpo_der2)

        layout_principal.addLayout(layout_titulo)
        layout_principal.addLayout(layout_cuerpo1)
        layout_principal.addLayout(layout_cuerpo2)

        #  _______________________________________________________________________________________
        # |                  Añadir el widget que contiene la imagen al layout principal          |
        # |_______________________________________________________________________________________|
        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def press_btnPokedex(self):
        if not self.pokedex_window:
            self.pokedex_window = Pokedex()

        self.hide() # Ocultar la ventana actual del menú
        self.pokedex_window.show() # Mostrar la ventana de la Pokédex
        print("Botón pkdex presionado")

def press_btnTipo():
    print("Botón tipo presionado")

def press_btnRivales():
    print("Botón rivals presionado")

def press_btnCombate():
    print("Botón combate presionado")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MenuPrincipal()
    ventana.show()
    sys.exit(app.exec())
