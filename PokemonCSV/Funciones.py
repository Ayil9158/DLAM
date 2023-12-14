import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtCore import Qt, QSize
import csv

#f9cb05 - amarillo
#396eb8 - azul
def get_styles():
    return """
        QMainWindow{
            /* Estilos para la ventana principal */
        }
        QComboBox {
            border: 1px solid;
            border-color: #f9cb05;
            width: 300px;
        }
        QGridLayout {
            border: 1px solid;
            border-color: #f9cb05;
        }
        #layout_titulo {
            text-align: left;
        }
    """

def Transform_IMG(path, scale_factor=1.0):
    image = QImage(path)

    # Ruta de la imagen por defecto en caso de error
    if image.isNull():
        path = "PokemonCSV/images/error.png"
        image = QImage(path)
    pixmap = QPixmap.fromImage(image)

    # Escalar la imagen según el factor de escala proporcionado
    new_width = int(pixmap.width() * scale_factor)
    new_height = int(pixmap.height() * scale_factor)
    pixmap = pixmap.scaled(new_width, new_height)

    label = QLabel()
    label.setPixmap(pixmap)
    # label.setAlignment(
    #         Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
    #     )
    return label

def dataset():
    ruta = 'PokemonCSV/datasets/pokedex_(Update.04.20).csv'
    num = 1
    name = 2
    german_name = 3
    japanese_name = 4
    generation = 5
    is_sub_legendary = 6
    is_legendary = 7
    is_mythical = 8
    classification = 9
    type_number = 10
    type1 = 11
    type2 = 12
    height_m = 13
    weight_kg =14
    abilities_number = 15
    ability_1 = 16
    ability_2 = 17
    ability_hidden = 18
    image = 41

    # Type defenses
    against_normal = 35
    against_fire = 36
    against_water = 37
    against_electric = 38
    against_grass = 39
    against_ice = 40
    against_fight = 41
    against_poison = 42
    against_ground = 43
    against_flying = 44
    against_psychic = 45
    against_bug = 46
    against_rock = 47
    against_ghost = 48
    against_dragon = 49
    against_dark = 50
    against_steel = 51
    against_fairy = 52

    # Base stats
    total_points = 19
    hp = 20
    spped = 25
    attack = 21
    defense = 22
    sp_attack = 23
    sp_defense = 24

    # Training
    catch_rate = 26
    base_friendship = 27
    base_experience = 28
    growth_rate =  29

    # Breeding
    egg_type_number = 30
    egg_type_1 = 31
    egg_type_2 = 32
    percentage_male = 33
    egg_cycles = 34

    # Menu - Pokedex
    num_list = []
    name_list = []

    # Left - Body
    type1_list = []
    type2_list = []
    against_normal_list = []
    against_fire_list = []
    against_water_list = []
    against_electric_list = []
    against_grass_list = []
    against_ice_list = []
    against_fight_list = []
    against_poison_list = []
    against_ground_list = []
    against_flying_list = []
    against_psychic_list = []
    against_bug_list = []
    against_rock_list = []
    against_ghost_list = []
    against_dragon_list = []
    against_dark_list = []
    against_steel_list = []
    against_fairy_list = []

    # Rigth - Body
    name_jap_list = []
    name_ge_list = []
    height_list = []
    weight_list = []
    abilities_number_list = []
    ability_1_list = []
    ability_2_list = []
    ability_hidden_list = []
    classification_list = []
    name_num = []

    required_indices = [num, name, type1, type2,
                        against_normal, against_fire ,against_water, against_electric,
                        against_grass, against_ice, against_fight, against_poison,
                        against_ground, against_flying, against_psychic, against_bug,
                        against_rock, against_ghost, against_dragon, against_dark,
                        against_steel, against_fairy,
                        japanese_name, german_name,
                        abilities_number, ability_1, ability_2, ability_hidden,
                        classification]

    with open(ruta, 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)

        for fila in lector_csv:
            if all(len(fila) > index for index in required_indices):
                pokemon_name = fila[name]
                if "Mega" not in pokemon_name:
                    number = str(fila[num]).zfill(3)
                    num_list.append(number)
                    name_list.append(pokemon_name)
                    name_num.append(f"{pokemon_name} N.°{number}")

                    type1_list.append(fila[type1])
                    type2_list.append(fila[type2])
                    against_normal_list.append(fila[against_normal])
                    against_fire_list.append(fila[against_fire])
                    against_water_list.append(fila[against_water])
                    against_electric_list.append(fila[against_electric])
                    against_grass_list.append(fila[against_grass])
                    against_ice_list.append(fila[against_ice])
                    against_fight_list.append(fila[against_fight])
                    against_poison_list.append(fila[against_poison])
                    against_ground_list.append(fila[against_ground])
                    against_flying_list.append(fila[against_flying])
                    against_psychic_list.append(fila[against_psychic])
                    against_bug_list.append(fila[against_bug])
                    against_rock_list.append(fila[against_rock])
                    against_ghost_list.append(fila[against_ghost])
                    against_dragon_list.append(fila[against_dragon])
                    against_dark_list.append(fila[against_dark])
                    against_steel_list.append(fila[against_steel])
                    against_fairy_list.append(fila[against_fairy])

                    name_jap_list.append(fila[japanese_name])
                    name_ge_list.append(fila[german_name])
                    classification_list.append(fila[classification])
    return (name_list, num_list, name_num, type1_list, type2_list,
            against_normal_list, against_fire_list, against_water_list, against_electric_list,
            against_grass_list, against_ice_list, against_fight_list, against_poison_list,
            against_ground_list, against_flying_list, against_psychic_list, against_bug_list,
            against_rock_list, against_ghost_list, against_dragon_list, against_dark_list,
            against_steel_list, against_fairy_list,
            name_jap_list, name_ge_list, classification_list)

def update_pokedex(poke_list, num_list, name_num,
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
                   poke_name_jap, name_jap_list, poke_name_ge, name_ge_list, poke_classification, classification_list):
        poke_selected = poke_list.currentIndex() # Obtener el índice seleccionado de la QComboBox

        # txt del índice
        txt_name_num = name_num[poke_selected]
        image_path = f"PokemonCSV/images/{num_list[poke_selected]}.png" # Construir la ruta de la imagen del Pokémon seleccionado

        txt_type1 = type1_list[poke_selected]
        txt_type2 = type2_list[poke_selected]
        ColorUtils.colors_type(txt_type1, poke_type1)
        if txt_type2 == "":
            poke_type2.setVisible(False)
        else:
            poke_type2.setVisible(True)
            ColorUtils.colors_type(txt_type2, poke_type2)

        txt_agn1 = [against_normal_list[poke_selected], "Normal"]
        txt_agn2 = [against_fire_list[poke_selected], "Fire"]
        txt_agn3 = [against_water_list[poke_selected], "Water"]
        txt_agn4 = [against_electric_list[poke_selected], "Electric"]
        txt_agn5 = [against_grass_list[poke_selected], "Grass"]
        txt_agn6 = [against_ice_list[poke_selected], "Ice"]
        txt_agn7 = [against_fight_list[poke_selected], "Fight"]
        txt_agn8 = [against_poison_list[poke_selected], "Poison"]
        txt_agn9 = [against_ground_list[poke_selected], "Ground"]
        txt_agn10 = [against_flying_list[poke_selected], "Flying"]
        txt_agn11 = [against_psychic_list[poke_selected], "Psychic"]
        txt_agn12 = [against_bug_list[poke_selected], "Bug"]
        txt_agn13 = [against_rock_list[poke_selected], "Rock"]
        txt_agn14 = [against_ghost_list[poke_selected], "Ghost"]
        txt_agn15 = [against_dragon_list[poke_selected], "Dragon"]
        txt_agn16 = [against_dark_list[poke_selected], "Dark"]
        txt_agn17 = [against_steel_list[poke_selected], "Steel"]
        txt_agn18 = [against_fairy_list[poke_selected], "Fairy"]
        ColorUtils.colors_against(txt_agn1, poke_agn1)
        ColorUtils.colors_against(txt_agn2, poke_agn2)
        ColorUtils.colors_against(txt_agn3, poke_agn3)
        ColorUtils.colors_against(txt_agn4, poke_agn4)
        ColorUtils.colors_against(txt_agn5, poke_agn5)
        ColorUtils.colors_against(txt_agn6, poke_agn6)
        ColorUtils.colors_against(txt_agn7, poke_agn7)
        ColorUtils.colors_against(txt_agn8, poke_agn8)
        ColorUtils.colors_against(txt_agn9, poke_agn9)
        ColorUtils.colors_against(txt_agn10, poke_agn10)
        ColorUtils.colors_against(txt_agn11, poke_agn11)
        ColorUtils.colors_against(txt_agn12, poke_agn12)
        ColorUtils.colors_against(txt_agn13, poke_agn13)
        ColorUtils.colors_against(txt_agn14, poke_agn14)
        ColorUtils.colors_against(txt_agn15, poke_agn15)
        ColorUtils.colors_against(txt_agn16, poke_agn16)
        ColorUtils.colors_against(txt_agn17, poke_agn17)
        ColorUtils.colors_against(txt_agn18, poke_agn18)
        against_buttons = [
            poke_agn1, poke_agn2, poke_agn3, poke_agn4, poke_agn5, poke_agn6,
            poke_agn7, poke_agn8, poke_agn9, poke_agn10, poke_agn11, poke_agn12,
            poke_agn13, poke_agn14, poke_agn15, poke_agn16, poke_agn17, poke_agn18
        ]
        row =  0
        col = 0
        for button in against_buttons:
            if button.isVisible():
                layout_against.addWidget(button, row, col)
                col += 1
                if col > 3:  # Cambia según el número de columnas que desees mostrar
                    col = 0
                    row += 1
            else:
                layout_against.removeWidget(button)



        txt_name_jap = name_jap_list[poke_selected]
        txt_name_ge = name_ge_list[poke_selected]
        txt_categoria = classification_list[poke_selected]

        # Actualizar el texto del QLabel
        pokemon.setText(f"{txt_name_num}")
        new_image = Transform_IMG(image_path, scale_factor=0.3)
        poke_image.setPixmap(new_image.pixmap())

        poke_type1.setText(f"{txt_type1}")
        poke_type2.setText(f"{txt_type2}")

        poke_name_jap.setText(f"Japanese Name: {txt_name_jap}")
        poke_name_ge.setText(f"German Name: {txt_name_ge}")
        poke_classification.setText(f"Classification: {txt_categoria}")

class ColorPalette:
    normal = QColor(164, 172, 175)
    fire = QColor(253, 125, 36)
    water = QColor(69, 146, 196)
    electric = QColor(238, 213, 53)
    grass = QColor(155, 204, 80)
    ice = QColor(81, 196, 231)
    fight = QColor(213, 103, 35)
    poison = QColor(185, 127, 201)
    ground = QColor(247, 222, 63)
    flying = QColor(61, 199, 239)
    psychic = QColor(243, 102, 185)
    bug = QColor(114, 159, 63)
    rock = QColor(163, 140, 33)
    ghost = QColor(123, 98, 163)
    dragon = QColor(241, 110, 87)
    dark = QColor(112, 112, 112)
    steel = QColor(158, 183, 184)
    fairy = QColor(253, 185, 233)
    no_type = QColor(255, 255, 255)


class ColorUtils:
    def set_button_color(button, color):
        button.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")

    def colors_against(txt_type, poke_type):
        color_palette = ColorPalette()
        type = txt_type[1]
        agn = txt_type[0]
        if agn == "2":
            if type == "Normal":
                ColorUtils.set_button_color(poke_type, color_palette.normal)
            elif type == "Fire":
                ColorUtils.set_button_color(poke_type, color_palette.fire)
            elif type == "Water":
                ColorUtils.set_button_color(poke_type, color_palette.water)
            elif type == "Electric":
                ColorUtils.set_button_color(poke_type, color_palette.electric)
            elif type == "Grass":
                ColorUtils.set_button_color(poke_type, color_palette.grass)
            elif type == "Ice":
                ColorUtils.set_button_color(poke_type, color_palette.ice)
            elif type == "Fight":
                ColorUtils.set_button_color(poke_type, color_palette.fight)
            elif type == "Poison":
                ColorUtils.set_button_color(poke_type, color_palette.poison)
            elif type == "Ground":
                ColorUtils.set_button_color(poke_type, color_palette.ground)
            elif type == "Flying":
                ColorUtils.set_button_color(poke_type, color_palette.flying)
            elif type == "Psychic":
                ColorUtils.set_button_color(poke_type, color_palette.psychic)
            elif type == "Bug":
                ColorUtils.set_button_color(poke_type, color_palette.bug)
            elif type == "Rock":
                ColorUtils.set_button_color(poke_type, color_palette.rock)
            elif type == "Ghost":
                ColorUtils.set_button_color(poke_type, color_palette.ghost)
            elif type == "Dragon":
                ColorUtils.set_button_color(poke_type, color_palette.dragon)
            elif type == "Dark":
                ColorUtils.set_button_color(poke_type, color_palette.dark)
            elif type == "Steel":
                ColorUtils.set_button_color(poke_type, color_palette.steel)
            elif type == "Fairy":
                ColorUtils.set_button_color(poke_type, color_palette.fairy)
            else:
                ColorUtils.set_button_color(poke_type, color_palette.no_type)
            poke_type.setVisible(True)
        else:
            poke_type.setVisible(False)
        return poke_type

    def colors_type(txt_type, poke_type):
        color_palette = ColorPalette()
        color_type = txt_type

        if color_type == "Normal":
            ColorUtils.set_button_color(poke_type, color_palette.normal)
            # set_button_color(poke_type, normal)
        elif color_type == "Fire":
            ColorUtils.set_button_color(poke_type, color_palette.fire)
            # set_button_color(poke_type, fire)
        elif color_type == "Water":
            ColorUtils.set_button_color(poke_type, color_palette.water)
            # set_button_color(poke_type, water)
        elif color_type == "Electric":
            ColorUtils.set_button_color(poke_type, color_palette.electric)
            # set_button_color(poke_type, electric)
        elif color_type == "Grass":
            ColorUtils.set_button_color(poke_type, color_palette.grass)
            # set_button_color(poke_type, grass)
        elif color_type == "Ice":
            ColorUtils.set_button_color(poke_type, color_palette.ice)
            # set_button_color(poke_type, ice)
        elif color_type == "Fight":
            ColorUtils.set_button_color(poke_type, color_palette.fight)
            # set_button_color(poke_type, fight)
        elif color_type == "Poison":
            ColorUtils.set_button_color(poke_type, color_palette.poison)
            # set_button_color(poke_type, poison)
        elif color_type == "Ground":
            ColorUtils.set_button_color(poke_type, color_palette.ground)
            # set_button_color(poke_type, ground)
        elif color_type == "Flying":
            ColorUtils.set_button_color(poke_type, color_palette.flying)
            # set_button_color(poke_type, flying)
        elif color_type == "Psychic":
            ColorUtils.set_button_color(poke_type, color_palette.psychic)
            # set_button_color(poke_type, psychic)
        elif color_type == "Bug":
            ColorUtils.set_button_color(poke_type, color_palette.bug)
            # set_button_color(poke_type, bug)
        elif color_type == "Rock":
            ColorUtils.set_button_color(poke_type, color_palette.rock)
            # set_button_color(poke_type, rock)
        elif color_type == "Ghost":
            ColorUtils.set_button_color(poke_type, color_palette.ghost)
            # set_button_color(poke_type, ghost)
        elif color_type == "Dragon":
            ColorUtils.set_button_color(poke_type, color_palette.dragon)
            # set_button_color(poke_type, dragon)
        elif color_type == "Dark":
            ColorUtils.set_button_color(poke_type, color_palette.dark)
            # set_button_color(poke_type, dark)
        elif color_type == "Steel":
            ColorUtils.set_button_color(poke_type, color_palette.steel)
            # set_button_color(poke_type, steel)
        elif color_type == "Fairy":
            ColorUtils.set_button_color(poke_type, color_palette.fairy)
            # set_button_color(poke_type, fairy)
        else:
            ColorUtils.set_button_color(poke_type, color_palette.no_type)
            # set_button_color(poke_type, no_type)

        return poke_type
