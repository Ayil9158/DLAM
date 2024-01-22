import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox, QGridLayout
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize

import Funciones

class PokedexGrid(QMainWindow):
    def __init__(self):
        super(PokedexGrid, self).__init__()

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
        layout_cuerpo = QGridLayout()

        (name_list, num_list, name_num,
            total_points_list, hp_list, attack_list, defense_list,
            sp_attack_list, sp_defense_list, speed_list,
            name_jap_list, name_ge_list,
            height_list, weight_list, classification_list,
            ability_1_list, ability_2_list, ability_hidden_list,
            type1_list, type2_list,
            against_normal_list, against_fire_list, against_water_list, against_electric_list,
            against_grass_list, against_ice_list, against_fight_list, against_poison_list,
            against_ground_list, against_flying_list, against_psychic_list, against_bug_list,
            against_rock_list, against_ghost_list, against_dragon_list, against_dark_list,
            against_steel_list, against_fairy_list) = Funciones.dataset()

        #  _______________________________________________________________________________________
        # |                  Parte superior del layout cuerpo                                     |
        # |_______________________________________________________________________________________|
        # Zona izquierda -
        layout_izq_sup = QVBoxLayout()

        poke_reg = QLabel('Bulbasaur N.001')
        path_image = "PokemonCSV/images/pokeball.png"
        poke_image = Funciones.Transform_IMG(path_image, scale_factor=0.3)

        layout_izq_sup.addWidget(poke_reg)
        layout_izq_sup.addWidget(poke_image)

        # Zona derecha
        layout_der_sup = QVBoxLayout()

        poke_name_jap = QLabel('Japanese Name: ')
        poke_name_ge = QLabel('German Name: ')

        container_layout_data = QWidget()
        layout_data = QGridLayout()
        poke_height = QLabel('Height: ')
        poke_weight = QLabel('Weight: ')
        poke_classification_txt = QLabel('Classification:')
        poke_classification = QLabel()
        poke_abilities_txt = QLabel('Abilities:')
        poke_ability1 = QLabel('1.- ')
        poke_ability2 = QLabel('2.- ')
        poke_ability_hidden = QLabel('Hidden - ')
        layout_data.addWidget(poke_height,0,0)
        layout_data.addWidget(poke_weight,1,0)
        layout_data.addWidget(poke_classification_txt,2,0)
        layout_data.addWidget(poke_classification,3,0)
        layout_data.addWidget(poke_abilities_txt,0,1)
        layout_data.addWidget(poke_ability1,1,1)
        layout_data.addWidget(poke_ability2,2,1)
        layout_data.addWidget(poke_ability_hidden,3,1)
        container_layout_data.setLayout(layout_data)
        container_layout_data.setObjectName('id_container_layout_data')

        layout_der_sup.addWidget(poke_name_jap)
        layout_der_sup.addWidget(poke_name_ge)
        layout_der_sup.addWidget(container_layout_data)

        #  _______________________________________________________________________________________
        # |                  Parte inferior del layout cuerpo                                     |
        # |_______________________________________________________________________________________|
        # Zona izquierda
        layout_izq_inf = QVBoxLayout()

        container_layout_stats = QWidget()
        lbl_total_points = QLabel("Total Base Points: ")
        layout_stats = QGridLayout()
        bar_hp = QLabel()
        # bar_hp = Funciones.CreateBar.set_bar_specifications()
        lbl_hp = QLabel("HP")
        bar_atk = QLabel()
        lbl_atk = QLabel("ATK")
        bar_def = QLabel()
        lbl_def = QLabel("DEF")
        bar_spatk = QLabel()
        lbl_spatk = QLabel("SP ATK")
        bar_spdef = QLabel()
        lbl_spdef = QLabel("SP DEF")
        bar_speed = QLabel()
        lbl_speed = QLabel("SEEP")

        # bar_hp.setFixedSize(45,100)
        # bar_atk.setFixedSize(45,100)
        # bar_def.setFixedSize(45,100)
        # bar_spatk.setFixedSize(45,100)
        # bar_spdef.setFixedSize(45,100)
        # bar_speed.setFixedSize(45,100)

        # bar_hp.setStyleSheet(f"background-color: white;")
        # bar_atk.setStyleSheet(f"background-color: white;")
        # bar_def.setStyleSheet(f"background-color: white;")
        # bar_spatk.setStyleSheet(f"background-color: white;")
        # bar_spdef.setStyleSheet(f"background-color: white;")
        # bar_speed.setStyleSheet(f"background-color: white;")

        layout_stats.addWidget(bar_hp,1,0)
        layout_stats.addWidget(bar_atk,1,1)
        layout_stats.addWidget(bar_def,1,2)
        layout_stats.addWidget(bar_spatk,1,3)
        layout_stats.addWidget(bar_spdef,1,4)
        layout_stats.addWidget(bar_speed,1,5)
        layout_stats.addWidget(lbl_hp,2,0)
        layout_stats.addWidget(lbl_atk,2,1)
        layout_stats.addWidget(lbl_def,2,2)
        layout_stats.addWidget(lbl_spatk,2,3)
        layout_stats.addWidget(lbl_spdef,2,4)
        layout_stats.addWidget(lbl_speed,2,5)
        layout_stats.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        # layout_stats.setAlignment(Qt.AlignmentFlag.AlignAbsolute)

        container_layout_stats.setLayout(layout_stats)
        container_layout_stats.setObjectName('id_container_layout_stats')

        layout_izq_inf.addWidget(lbl_total_points)
        layout_izq_inf.addWidget(container_layout_stats)

        # Zona derecha
        layout_der_inf = QVBoxLayout()

        layout_type = QHBoxLayout()
        poke_tipo_txt = QLabel('Type:')
        poke_type1 = QPushButton('None')
        poke_type2 = QPushButton('None')
        layout_type.addWidget(poke_type1)
        layout_type.addWidget(poke_type2)
        layout_type.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout_against = QGridLayout()
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
        layout_against.addWidget(poke_agn4,1,0)
        layout_against.addWidget(poke_agn5,1,1)
        layout_against.addWidget(poke_agn6,1,2)
        layout_against.addWidget(poke_agn7,2,0)
        layout_against.addWidget(poke_agn8,2,1)
        layout_against.addWidget(poke_agn9,2,2)
        layout_against.addWidget(poke_agn10,3,0)
        layout_against.addWidget(poke_agn11,3,1)
        layout_against.addWidget(poke_agn12,3,2)
        layout_against.addWidget(poke_agn13,4,0)
        layout_against.addWidget(poke_agn14,4,1)
        layout_against.addWidget(poke_agn15,4,2)
        layout_against.addWidget(poke_agn16,5,0)
        layout_against.addWidget(poke_agn17,5,1)
        layout_against.addWidget(poke_agn18,5,2)
        layout_against.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout_der_inf.addWidget(poke_tipo_txt)
        layout_der_inf.addLayout(layout_type)
        layout_der_inf.addWidget(poke_against_txt)
        layout_der_inf.addLayout(layout_against)
        layout_der_inf.addWidget(poke_against_txt)

        #  _______________________________________________________________________________________
        # |                  Contenido del layout menu                                            |
        # |_______________________________________________________________________________________|
        poke_list = QComboBox(self)
        poke_list.addItems(name_list)
        poke_list.currentIndexChanged.connect(lambda: Funciones.update_pokedex(poke_list, num_list, name_num, poke_image, poke_reg,
                   lbl_total_points, total_points_list, bar_hp, hp_list, bar_atk, attack_list,
                   bar_def, defense_list, bar_spatk, sp_attack_list, bar_spdef, sp_defense_list,
                   bar_speed, speed_list,
                   poke_name_jap, name_jap_list, poke_name_ge, name_ge_list, layout_data,
                   poke_height, height_list, poke_weight, weight_list,
                   poke_classification, classification_list, poke_ability1, ability_1_list,
                   poke_ability2, ability_2_list, poke_ability_hidden, ability_hidden_list,
                   poke_type1, type1_list, poke_type2, type2_list, layout_against,
                   poke_agn1, against_normal_list, poke_agn2, against_fire_list,
                   poke_agn3, against_water_list, poke_agn4, against_electric_list,
                   poke_agn5, against_grass_list, poke_agn6, against_ice_list,
                   poke_agn7, against_fight_list, poke_agn8, against_poison_list,
                   poke_agn9, against_ground_list, poke_agn10, against_flying_list,
                   poke_agn11, against_psychic_list, poke_agn12, against_bug_list,
                   poke_agn13, against_rock_list, poke_agn14, against_ghost_list,
                   poke_agn15, against_dragon_list, poke_agn16, against_dark_list,
                   poke_agn17, against_steel_list, poke_agn18, against_fairy_list))
        poke_list.setObjectName('id_poke')
        before_pokemon = QPushButton('Pokemon anterior')
        before_pokemon.setObjectName('id_button_selection')
        after_pokemon = QPushButton('Pokemon siguiente')
        after_pokemon.setObjectName('id_button_selection')

        layout_menu.addWidget(before_pokemon)
        layout_menu.addWidget(after_pokemon)

        #  _______________________________________________________________________________________
        # |                  Añadir los layouts faltantes hasta llegar al principal               |
        # |_______________________________________________________________________________________|
        layout_cuerpo.addLayout(layout_izq_sup,0,0)
        layout_cuerpo.addLayout(layout_der_sup,0,1)
        layout_cuerpo.addLayout(layout_izq_inf,1,0)
        layout_cuerpo.addLayout(layout_der_inf,1,1)

        #layout_principal.addLayout(layout_titulo)
        layout_principal.addLayout(layout_menu)
        layout_principal.addWidget(poke_list)
        layout_principal.addLayout(layout_cuerpo)

        #  _______________________________________________________________________________________
        # |                  Añadir el widget que contiene la imagen al layout principal          |
        # |_______________________________________________________________________________________|
        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PokedexGrid()
    ventana.show()
    sys.exit(app.exec())