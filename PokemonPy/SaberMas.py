# VENTANA DE SABER MÁS - INFORMACIÓN DETALLADA DE LOS POKEMONS

from kivy.app import App
from kivy.uix.button import Button # Importa la clase Button del módulo
from kivy.uix.boxlayout import BoxLayout  # Importa la clase BoxLayout del módulo (hara de Panel)
from kivy.uix.image import Image  # Importa la clase Image del módulo
from kivy.uix.spinner import Spinner # Importa la clase Spinner del módulo (hara de MenuOption)
from kivy.uix.label import Label # Importa la clase Label del módulo

import Pokedex
# pkdex = Pokedex.Pokedex_main.build

# Define una nueva clase llamada pokemenu que hereda de la clase App.
class Saber_Mas(App):
    # Este método es obligatorio en cualquier clase de aplicación Kivy
    # Se llama automáticamente cuando se inicia la aplicación
    def build(self):
        # *****************************************************************************************
        #                    Crea un layout principal para organizar los layouts                  *
        # *****************************************************************************************
        layout_principal = BoxLayout(orientation='vertical')

        # Primer layout - titulo (ocupa todo lo de arriba)
        layout_titulo = BoxLayout(orientation='horizontal', size_hint_y=0.2)
        titulo = Label(text='POKEDEX')
        layout_titulo.add_widget(titulo)

        # *****************************************************************************************
        #                    Segundo layout - cuerpo1 (ocupa lo demás de arriba)                  *
        # *****************************************************************************************
        layout_cuerpo1 = BoxLayout(orientation='horizontal', size_hint_y=0.4)

        layout_cuerpo_izq1 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        img_pkmn = Pokedex.img_seleccion_pkmn(Pokedex.Spinner)
        layout_cuerpo_izq1.add_widget(img_pkmn)

        layout_cuerpo_der1 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        summ_pkmn = Pokedex.actualizar_info(Pokedex.Spinner)
        layout_cuerpo_der1.add_widget(summ_pkmn)

        layout_cuerpo1.add_widget(layout_cuerpo_izq1)
        layout_cuerpo1.add_widget(layout_cuerpo_der1)

        # *****************************************************************************************
        #                    Tercer layout - cuerpo2 (ocupa lo demás de arriba)                   *
        # *****************************************************************************************
        layout_cuerpo2 = BoxLayout(orientation='horizontal', size_hint_y=0.4)

        layout_cuerpo_izq2 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        pts_base = Label(text='Puntos Base')
        layout_cuerpo_izq2.add_widget(pts_base)

        layout_cuerpo_der2 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        tipo_pkmn = Pokedex.tipo_seleccion_pkmn(Pokedex.Spinner)
        layout_cuerpo_der2.add_widget(tipo_pkmn)

        layout_cuerpo2.add_widget(layout_cuerpo_izq2)
        layout_cuerpo2.add_widget(layout_cuerpo_der2)

        return layout_principal

if __name__ == '__main__':
    Saber_Mas().run()