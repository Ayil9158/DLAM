import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox, QGridLayout
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize

import Funciones

class Pokedex(QMainWindow):
    def __init__(self):
        super(Pokedex, self).__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Pokedex")
        self.setGeometry(100, 100, 700, 500) # (x, y, ancho, alto)
        estilos = Funciones.get_styles()
        self.setStyleSheet(estilos)

        #  _______________________________________________________________________________________
        # |                  Creación de layouts contenedores                                     |
        # |_______________________________________________________________________________________|
        layout_principal = QVBoxLayout()

        layout_titulo = QHBoxLayout()
        titulo = Funciones.Transform_IMG('PokemonCSV/images/titulo_pokedex.png')
        titulo.setFixedHeight(110)
        titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        layout_titulo.addWidget(titulo)
        layout_menu = QHBoxLayout()
        layout_cuerpo = QHBoxLayout()

        (name_list, num_list, name_num, type1_list, type2_list,
            against_normal_list, against_fire_list, against_water_list, against_electric_list,
            against_grass_list, against_ice_list, against_fight_list, against_poison_list,
            against_ground_list, against_flying_list, against_psychic_list, against_bug_list,
            against_rock_list, against_ghost_list, against_dragon_list, against_dark_list,
            against_steel_list, against_fairy_list,
            name_jap_list, name_ge_list, classification_list) = Funciones.dataset()

        #  _______________________________________________________________________________________
        # |                  Parte derecha del layout cuerpo                                      |
        # |_______________________________________________________________________________________|
        layout_cuerpo_derecho = QVBoxLayout()

        poke_name_jap = QLabel('Japanese Name: ')
        poke_name_ge = QLabel('German Name: ')

        layout_data = QGridLayout()
        poke_height = QLabel('Height: ')
        poke_weight = QLabel('weight: ')
        poke_abilities = QLabel('Abilitie: ')
        poke_classification = QLabel('Classification: ')

        layout_cuerpo_derecho.addWidget(poke_name_jap)
        layout_cuerpo_derecho.addWidget(poke_name_ge)
        layout_cuerpo_derecho.addWidget(poke_abilities)
        layout_cuerpo_derecho.addWidget(poke_classification)

        #  _______________________________________________________________________________________
        # |                  Parte izquierda del layout cuerpo                                    |
        # |_______________________________________________________________________________________|
        layout_cuerpo_izquierdo = QVBoxLayout()

        pokemon = QLabel('Bulbasaur N.001')
        path_image = "PokemonCSV/images/pokeball.png"
        poke_image = Funciones.Transform_IMG(path_image, scale_factor=0.3)

        layout_type = QHBoxLayout()
        poke_tipo_txt = QLabel('Type:')
        poke_type1 = QPushButton('None')
        poke_type2 = QPushButton('None')
        layout_type.addWidget(poke_type1)
        layout_type.addWidget(poke_type2)
        layout_type.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout_against = QGridLayout()
        #layout_against = QVBoxLayout()
        poke_against_txt = QLabel('Against:')
        poke_agn1 = QPushButton('Normal')
        poke_agn2 = QPushButton('Fire')
        poke_agn3 = QPushButton('Water')
        poke_agn4 = QPushButton('Electric')
        poke_agn5 = QPushButton('Grass')
        poke_agn6 = QPushButton('Ice')
        poke_agn7 = QPushButton('Fight')
        poke_agn8 = QPushButton('Poison')
        poke_agn9 = QPushButton('Ground')
        poke_agn10 = QPushButton('Flying')
        poke_agn11 = QPushButton('Psychic')
        poke_agn12 = QPushButton('Bug')
        poke_agn13 = QPushButton('Rock')
        poke_agn14 = QPushButton('Ghost')
        poke_agn15 = QPushButton('Dragon')
        poke_agn16 = QPushButton('Dark')
        poke_agn17 = QPushButton('Steel')
        poke_agn18 = QPushButton('Fairy')
        layout_against.addWidget(poke_agn1,0,0)
        layout_against.addWidget(poke_agn2,0,1)
        layout_against.addWidget(poke_agn3,0,2)
        layout_against.addWidget(poke_agn4,0,3)
        layout_against.addWidget(poke_agn5,1,0)
        layout_against.addWidget(poke_agn6,1,1)
        layout_against.addWidget(poke_agn7,1,2)
        layout_against.addWidget(poke_agn8,1,3)
        layout_against.addWidget(poke_agn9,2,0)
        layout_against.addWidget(poke_agn10,2,1)
        layout_against.addWidget(poke_agn11,2,2)
        layout_against.addWidget(poke_agn12,2,3)
        layout_against.addWidget(poke_agn13,3,0)
        layout_against.addWidget(poke_agn14,3,1)
        layout_against.addWidget(poke_agn15,3,2)
        layout_against.addWidget(poke_agn16,3,3)
        layout_against.addWidget(poke_agn17,4,0)
        layout_against.addWidget(poke_agn18,4,1)
        layout_against.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout_cuerpo_izquierdo.addWidget(pokemon)
        layout_cuerpo_izquierdo.addWidget(poke_image)
        layout_cuerpo_izquierdo.addWidget(poke_tipo_txt)
        layout_cuerpo_izquierdo.addLayout(layout_type)
        layout_cuerpo_izquierdo.addWidget(poke_against_txt)
        layout_cuerpo_izquierdo.addLayout(layout_against)
        layout_cuerpo_izquierdo.addWidget(poke_against_txt)

        #  _______________________________________________________________________________________
        # |                  Contenido del layout menu                                            |
        # |_______________________________________________________________________________________|
        before_pokemon = QPushButton('Pokemon anterior')
        poke_list = QComboBox()
        poke_list.addItems(name_list)
        poke_list.currentIndexChanged.connect(lambda: Funciones.update_pokedex(poke_list, num_list, name_num,
                   poke_image, pokemon, poke_type1, type1_list, poke_type2, type2_list, layout_against,
                   poke_agn1, against_normal_list, poke_agn2, against_fire_list,
                   poke_agn3, against_water_list, poke_agn4, against_electric_list,
                   poke_agn5, against_grass_list, poke_agn6, against_ice_list,
                   poke_agn7, against_fight_list, poke_agn8, against_poison_list,
                   poke_agn9, against_ground_list, poke_agn10, against_flying_list,
                   poke_agn11, against_psychic_list, poke_agn12, against_bug_list,
                   poke_agn13, against_rock_list, poke_agn14, against_ghost_list,
                   poke_agn15, against_dragon_list, poke_agn16, against_dark_list,
                   poke_agn17, against_steel_list, poke_agn18, against_fairy_list,
                   poke_name_jap, name_jap_list, poke_name_ge, name_ge_list, poke_classification, classification_list))
        # poke_list.setStyleSheet(estilos)
        after_pokemon = QPushButton('Pokemon siguiente')

        layout_menu.addWidget(before_pokemon)
        layout_menu.addWidget(poke_list)
        layout_menu.addWidget(after_pokemon)

        #  _______________________________________________________________________________________
        # |                  Añadir los layouts faltantes hasta llegar al principal               |
        # |_______________________________________________________________________________________|
        layout_cuerpo.addLayout(layout_cuerpo_izquierdo)
        layout_cuerpo.addLayout(layout_cuerpo_derecho)

        #layout_principal.addLayout(layout_titulo)
        layout_principal.addLayout(layout_menu)
        layout_principal.addLayout(layout_cuerpo)

        #  _______________________________________________________________________________________
        # |                  Añadir el widget que contiene la imagen al layout principal          |
        # |_______________________________________________________________________________________|
        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Pokedex()
    ventana.show()
    sys.exit(app.exec())