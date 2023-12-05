from kivy.uix.button import Button # Importa la clase Button del módulo
from kivy.uix.image import Image  # Importa la clase Image del módulo
from kivy.uix.label import Label # Importa la clase Label del módulo

name_pkmn = {
    '001 - Bulbasaur':'001',
    '004 - Charmander':'004',
    '007 - Squirtle':'007'
}
# *****************************************************************************************
#                    TODOS LOS TIPOS POSIBLES                                             *
# *****************************************************************************************

tipo_acero = Button(text='Acero', background_color=(158/255, 183/255, 184/255, 1))
tipo_agua = Button(text='Agua', background_color=(69/255, 146/255, 196/255, 1))
tipo_bicho = Button(text='Bicho', background_color=(114/255, 159/255, 63/255, 1))
tipo_dragon = Button(text='Dragon', background_color=(241/255, 110/255, 87/255, 1)) # Azul: 83, 164, 207
tipo_electrico  = Button(text='Eléctrico', background_color=(238/255, 213/255, 53/255, 1))
tipo_fantasma  = Button(text='Fantasma', background_color=(123/255, 98/255, 163/255, 1))
tipo_fuego  = Button(text='Fuego', background_color=(253/255, 125/255, 36/255, 1))
tipo_hada  = Button(text='Hada', background_color=(253/255, 185/255, 233/255, 1))
tipo_hielo  = Button(text='Hielo', background_color=(81/255, 196/255, 231/255, 1))
tipo_lucha  = Button(text='Lucha', background_color=(213/255, 103/255, 35/255, 1))
tipo_normal  = Button(text='Normal', background_color=(164/255, 172/255, 175/255, 1))
tipo_planta = Button(text='Planta', background_color=(155/255, 204/255, 80/255, 1))
tipo_psiquico  = Button(text='Psiquico', background_color=(243/255, 102/255, 185/255, 1))
tipo_roca  = Button(text='Roca', background_color=(163/255, 140/255, 33/255, 1))
tipo_siniestro  = Button(text='Siniestro', background_color=(112/255, 112/255, 112/255, 1))
tipo_tierra  = Button(text='Tierra', background_color=(247/255, 222/255, 63/255, 1)) # Cafe 171, 152, 66
tipo_veneno  = Button(text='Veneno', background_color=(185/255, 127/255, 201/255, 1))
tipo_volador = Button(text='Volador', background_color=(61/255, 199/255, 239/255, 1)) # Gris 189, 185, 184
tipo_sintipo = Button(text='None', background_color=(1, 0, 0, 1))

# *****************************************************************************************
#                    TODAS LAS HABILIDADES POSIBLES                                       *
# *****************************************************************************************

espesura = Label(text='Potencia sus movimientos de tipo Planta cuando le quedan pocos PS.')


# *****************************************************************************************
#                    IMAGEN QUE SE MUESTRA SEGUN LA LISTA                                 *
# *****************************************************************************************
def img_seleccion_pkmn(pokemon):
    valor = name_pkmn.get(pokemon, 'No encontrado')
    if valor == '001':
        return Image(source='imagenes/001.png')
    elif valor == '004':
        return Image(source='imagenes/004.png')
    elif valor == '007':
        return Image(source='imagenes/007.png')
    else:
        return Image(source='imagenes/pokeball.png')  # Imagen default o para Pokémon desconocido

# *****************************************************************************************
#                    BREVE DESCRIPCIÓN QUE SE MUESTRA SEGUN LA LISTA                      *
# *****************************************************************************************
def info_seleccion_pkmn(pokemon):
    valor = name_pkmn.get(pokemon, 'No encontrado')
    if valor == '001':
        descripcion = Label(text='Este Pokémon nace con una semilla en el lomo, que brota con el paso del tiempo.')
    elif valor == '004':
        descripcion = Label(text='Prefiere las cosas calientes. Dicen que cuando llueve le sale vapor de la punta de la cola.')
    elif valor == '007':
        descripcion = Label(text='Cuando retrae su largo cuello en el caparazón, dispara agua a una presión increíble.')
    else:
        descripcion = Label(text='Descripción')
    descripcion.halign = 'left'
    descripcion.text_size = (225, None)
    return descripcion

# *****************************************************************************************
#                    TIPO QUE SE MUESTRA SEGUN LA LISTA                                   *
# *****************************************************************************************
def tipo_seleccion_pkmn(pokemon):
    valor = name_pkmn.get(pokemon, 'No encontrado')
    tipo1 = Button(text='???', background_color=(1, 0, 0, 1))
    if valor == '001':
        # tipo1 = Button(text='Planta', background_color=(1, 0, 0, 1))
        tipo1 = tipo_planta
    elif valor == '004':
        tipo1 = tipo_fuego
    elif valor == '007':
        tipo1 = tipo_agua
    tipo1.disabled = True
    tipo1.opacity = 5
    tipo1.size_hint_y = 0.5
    tipo1.pos_hint = {'x': 1, 'top': 0.5}
    return tipo1

def tipo_seleccion_pkmn2(pokemon):
    valor = name_pkmn.get(pokemon, 'No encontrado')
    tipo2 = Button(text='???', background_color=(1, 0, 0, 1))
    if valor == '001':
        tipo2 = tipo_veneno
    elif valor == '004':
        tipo2 = tipo_sintipo
    elif valor == '007':
        tipo2 = tipo_sintipo
    tipo2.disabled = True
    tipo2.opacity = 5
    tipo2.size_hint_y = 0.5
    tipo2.pos_hint = {'x': 1, 'top': 0.5}
    return tipo2

# --------------------------- INFORMACIÓN EXTENDIDA -----------------------------------------------
def bulbasaur():
    pokemon = Image(source='imagenes/001.png')
    descripcion_azul = Label(text='Este Pokémon nace con una semilla en el lomo, que brota con el paso del tiempo.')
    descripcion_rojo = Label(text='Desde que nace, crece alimentándose de los nutrientes que contiene la semilla de su lomo.')
    altura = Label(text='0.7m')
    peso = Label(text='6.9kg')
    categoria = Label(text='Semilla')
    habilidad = Label(text='Espesura')
    info_habilidad = espesura
    tipo1 = tipo_planta
    tipo2 = tipo_veneno
    debilidad1 = tipo_fuego
    debilidad2 = tipo_psiquico
    debilidad3 = tipo_volador
    debilidad4 = tipo_hielo
def evol_bulbasaur():
    evolucion_1 = Image(source='imagenes/001.png')
    evolucion_2 = Image(source='imagenes/002.png')
    evolucion_3 = Image(source='imagenes/003.png')
