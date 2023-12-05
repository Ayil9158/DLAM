# VENTANA PRINCIPAL A LAS DEMAS VENTANAS

from kivy.app import App
from kivy.uix.button import Button # Importa la clase Button del módulo
from kivy.uix.boxlayout import BoxLayout  # Importa la clase BoxLayout del módulo (hara de Panel)
from kivy.uix.label import Label # Importa la clase Label del módulo
from kivy.uix.image import Image  # Importa la clase Image del módulo


class menuprincipal_main(App):
    # Este método es obligatorio en cualquier clase de aplicación Kivy
    # Se llama automáticamente cuando se inicia la aplicación
    def build(self):
        # *****************************************************************************************
        #                    Crea un layout principal para organizar los layouts                  *
        # *****************************************************************************************
        layout_principal = BoxLayout(orientation='vertical')

        # Primer layout - titulo (ocupa todo lo de arriba)
        layout_titulo = BoxLayout(orientation='horizontal', size_hint_y=0.2)
        titulo = Image(source='imagenes/titulo_pokedex.png')
        layout_titulo.add_widget(titulo)

        # *****************************************************************************************
        #                    Segundo layout - cuerpo1 (ocupa lo demás de arriba)                  *
        # *****************************************************************************************
        layout_cuerpo1 = BoxLayout(orientation='horizontal', size_hint_y=0.4)

        layout_cuerpo_izq1 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        imgPokedex = Image(source='imagenes/pokedex.png')
        btnPokedex = Button(text='Pokedex', background_color=(66/255, 98/255, 171/255, 1), size_hint=(0.7, 0.5), pos_hint = {'x': 0.15, 'top': 1})
        btnPokedex.bind(on_press=self.press_pokedex)
        layout_cuerpo_izq1.add_widget(imgPokedex)
        layout_cuerpo_izq1.add_widget(btnPokedex)

        layout_cuerpo_der1 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        imgTipo = Image(source='imagenes/tablatipo.png')
        btnTipo = Button(text='Movimientos', background_color=(229/255, 171/255, 22/255, 1), background_normal='', size_hint=(0.7, 0.5), pos_hint = {'x': 0.15, 'top': 1})
        btnTipo.bind()
        layout_cuerpo_der1.add_widget(imgTipo)
        layout_cuerpo_der1.add_widget(btnTipo)

        # *****************************************************************************************
        #                    Tercer layout - cuerpo2 (ocupa lo demás de abajo)                    *
        # *****************************************************************************************
        layout_cuerpo2 = BoxLayout(orientation='horizontal', size_hint_y=0.4)

        layout_cuerpo_izq2 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        imgEntrenadores = Image(source='imagenes/entrenadores.png')
        btnEntrenadores = Button(text='Entrenadores', background_color=(52/255, 135/255, 106/255, 1), background_normal='', size_hint=(0.7, 0.5), pos_hint = {'x': 0.15, 'top': 1})
        btnEntrenadores.bind()
        layout_cuerpo_izq2.add_widget(imgEntrenadores)
        layout_cuerpo_izq2.add_widget(btnEntrenadores)

        layout_cuerpo_der2 = BoxLayout(orientation='vertical', spacing=20, padding=15)
        imgCombate = Image(source='imagenes/combate.png')
        btnCombate = Button(text='Combate', background_color=(229/255, 171/255, 22/255, 1), background_normal='', size_hint=(0.7, 0.5), pos_hint = {'x': 0.15, 'top': 1})
        btnCombate.bind()
        layout_cuerpo_der2.add_widget(imgCombate)
        layout_cuerpo_der2.add_widget(btnCombate)


        # *****************************************************************************************
        # *                  Agrega los layouts (der-izq) 1y2 al layout cuerpo 1y2                *
        # *****************************************************************************************
        layout_cuerpo1.add_widget(layout_cuerpo_izq1)
        layout_cuerpo1.add_widget(layout_cuerpo_der1)
        layout_cuerpo2.add_widget(layout_cuerpo_izq2)
        layout_cuerpo2.add_widget(layout_cuerpo_der2)

        # *****************************************************************************************
        # *                  Agrega los layouts al layout principal                               *
        # *****************************************************************************************
        layout_principal.add_widget(layout_titulo)
        layout_principal.add_widget(layout_cuerpo1)
        layout_principal.add_widget(layout_cuerpo2)

        return layout_principal  # Devuelve el layout en lugar de un solo botón

    def press_pokedex(self, instance):
        from Pokedex import Pokedex_main
        App.get_running_app().stop()  # Cierra la ventana actual de MenuPrincipal.py
        Pokedex_main().run() # Llama a la clase pokedex_main de Pokedex.py

# Esta línea verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    menuprincipal_main().run() # El método run() inicia la aplicación Kivy y entra en el bucle principal
