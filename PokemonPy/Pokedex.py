# VENTANA DE POKEDEX - RESUMEN DE LOS POKEMONS

from kivy.app import App
from kivy.uix.button import Button # Importa la clase Button del módulo
from kivy.uix.boxlayout import BoxLayout  # Importa la clase BoxLayout del módulo (hara de Panel)
# from kivy.uix.image import Image  # Importa la clase Image del módulo
from kivy.uix.spinner import Spinner # Importa la clase Spinner del módulo (hara de MenuOption)
from kivy.uix.label import Label # Importa la clase Label del módulo
# from kivy.graphics import Color, Rectangle
from kivy.core.window import Window


from PokeInfo import name_pkmn
from PokeInfo import img_seleccion_pkmn, info_seleccion_pkmn, tipo_seleccion_pkmn, tipo_seleccion_pkmn2

# Define una nueva clase llamada pokemenu que hereda de la clase App.
class Pokedex_main(App):

    def actualizar_imagen(self, instance, texto_seleccionado):
        nueva_imagen = img_seleccion_pkmn(texto_seleccionado)
        if hasattr(self, 'layout_imagen'):
            self.layout_imagen.clear_widgets()
            self.layout_imagen.add_widget(nueva_imagen)

    def actualizar_info(self, instance, texto_seleccionado):
        nuevo_summary = info_seleccion_pkmn(texto_seleccionado)
        if hasattr(self, 'layout_summary'):
            self.layout_summary.clear_widgets()  # Limpia los widgets del layout derecho
            self.layout_summary.add_widget(nuevo_summary)  # Agrega el nuevo Label con info

    def actualizar_tipo(self, instance, texto_seleccionado):
        nuevo_tipo1 = tipo_seleccion_pkmn(texto_seleccionado)
        nuevo_tipo2 = tipo_seleccion_pkmn2(texto_seleccionado)
        if hasattr(self, 'layout_tipo'):
            self.layout_tipo.clear_widgets()
            self.layout_tipo.add_widget(self.tipo_pkmn)
            if nuevo_tipo1.text != 'None':
                self.layout_tipo.add_widget(nuevo_tipo1)
            if nuevo_tipo2.text == 'None':
                tipo2 = Button(text='', background_color=(0, 0, 0, 1), size_hint_y=0.5, pos_hint = {'x': 1, 'top': 0.5})
                self.layout_tipo.add_widget(tipo2)
            elif nuevo_tipo2.text != 'None':
                self.layout_tipo.add_widget(nuevo_tipo2)

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

        # Segundo layout - cuerpo (ocupa lo demás)
        layout_cuerpo = BoxLayout(orientation='horizontal', size_hint_y=0.6)

        # Tercer layout - base (ocupa todo lo de abajo)
        layout_base = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=50, padding=35)
        btn_Volver = Button(text='Volver', size_hint=(0.4, 1), pos_hint = {'x': 0, 'top': 0.7})
        btn_Volver.bind(on_press=self.press_volver)
        btn_Info = Button(text='Saber más', size_hint=(0.4, 1), pos_hint = {'x': 1, 'top': 0.7})

        layout_base.add_widget(btn_Volver)
        layout_base.add_widget(btn_Info)


        # *****************************************************************************************
        # *                  PARTE DERECHA DEL CUERPO                                             *
        # *****************************************************************************************
        layout_cuerpo_derecho = BoxLayout(orientation='vertical')

        poke_list = Spinner(
            text='Selecciona un pokemon',  # Opción predeterminada
            values=(name_pkmn),  # Lista de opciones
            size_hint=(0.7, 0.15),
            # background_color=(1, 0, 0, 1), # BG rojo
            pos_hint = {'x': 0.15, 'top': 1}
            )
        poke_list.bind(text=self.actualizar_imagen)  # Vincula el evento on_text con la función actualizar_imagen
        poke_list.bind(text=self.actualizar_info)  # Vincula el evento on_text con la función actualizar_info
        poke_list.bind(text=self.actualizar_tipo)

        self.layout_summary = BoxLayout(orientation='vertical') # Crear panel para actualizar la descripcion
        summary = info_seleccion_pkmn(poke_list) # Crea un widget de label con info
        self.layout_summary.add_widget(summary)

        layout_cuerpo_derecho.add_widget(poke_list)
        layout_cuerpo_derecho.add_widget(self.layout_summary)


        # *****************************************************************************************
        #                    PARTE IZQUIERDA DEL CUERPO                                           *
        # *****************************************************************************************
        layout_cuerpo_izquierdo = BoxLayout(orientation='vertical', padding=35)

        self.layout_imagen = BoxLayout(orientation='vertical') # Crear panel para actualizar la imagen
        imagen = img_seleccion_pkmn(poke_list)   # Crea un widget de imagen segun spinner
        self.layout_imagen.add_widget(imagen)

        self.layout_tipo = BoxLayout(orientation='horizontal', size_hint_y=0.35)
        self.tipo_pkmn = Label(text='TIPO: ', size_hint_y=0.5, pos_hint = {'x': 0, 'top': 0.5})
        tipoa = tipo_seleccion_pkmn(poke_list)
        tipob = tipo_seleccion_pkmn2(poke_list)
        self.layout_tipo.add_widget(self.tipo_pkmn)
        self.layout_tipo.add_widget(tipoa)
        self.layout_tipo.add_widget(tipob)

        layout_cuerpo_izquierdo.add_widget(self.layout_imagen)
        layout_cuerpo_izquierdo.add_widget(self.layout_tipo)


        # *****************************************************************************************
        # *                  Agrega los layouts (der-izq) al layout cuerpo                        *
        # *****************************************************************************************
        layout_cuerpo.add_widget(layout_cuerpo_izquierdo)
        layout_cuerpo.add_widget(layout_cuerpo_derecho)

        # *****************************************************************************************
        # *                  Agrega los layouts al layout principal                               *
        # *****************************************************************************************
        layout_principal.add_widget(layout_titulo)
        layout_principal.add_widget(layout_cuerpo)
        layout_principal.add_widget(layout_base)

        return layout_principal  # Devuelve el layout en lugar de un solo botón

    def press_volver(self, instance):
        from MenuPrincipal import menuprincipal_main
        App.get_running_app().stop()  # Cierra la ventana actual de Pokedex2.py
        menuprincipal_main().run() # Llama a la clase menuprincipal_main de MenuPrincipal.py

    def on_start(self):
        # Establece el ancho y el alto mínimo de la ventana para evitar redimensionar
        Window.minimum_width, Window.minimum_height = Window.size
        Window.maximum_width, Window.maximum_height = 800, 600

        # Otra opción si prefieres bloquear la redimensión incluso si el contenido cambia:
        Window.bind(width=self.prevent_resize, height=self.prevent_resize)

    def prevent_resize(self, instance, value):
        # Evita que la ventana cambie de tamaño
        return Window.size


# Esta línea verifica si el script se está ejecutando directamente
if __name__ == '__main__':
    Pokedex_main().run() # El método run() inicia la aplicación Kivy y entra en el bucle principal
