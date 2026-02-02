# Ventana que:
# * Se encoge a una sola "linea" vertical
# * No congela la IU
# * Sonido retro (8-bit-game-2.wav)
# * Cierre pixeleado (escalonado)
# * Deshabilita el boton de cierre al iniciar la animación
# * Destruye la ventana (si close)

import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer, QRect, QUrl
from PyQt5.QtMultimedia import QSoundEffect

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRT Retro")
        self.setGeometry(300, 200, 400, 300)

        # Botón X
        self.boton_x = QPushButton("X", self)
        self.boton_x.setFixedSize(30, 30)
        self.boton_x.move(360, 10)
        self.boton_x.clicked.connect(self.apagado_retro)

        # Sonido retro
        ruta = os.path.abspath("/ProgramasPropios/ORV/Menu_Direct/System/Sounds/8-bit-game-2.wav")
        # print(ruta, os.path.exists(ruta))
        self.sonido = QSoundEffect(self)
        self.sonido.setSource(QUrl.fromLocalFile(ruta))
        self.sonido.setVolume(0.5)

        # Timer para efecto escalonado
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.frame_apagado)
        self.pasos = 15  # más pasos = más “pixelado”

    def apagado_retro(self):
        self.boton_x.setEnabled(False) # Deshabilitar boton para que no suene de nuevo
        self.rect_actual = self.geometry()
        self.paso_actual = 0
        self.sonido.play()
        self.timer.start(30)  # ms entre frames

    def frame_apagado(self):
        if self.paso_actual >= self.pasos:
            self.timer.stop()
            self.close()  # self.hide()
            # self.boton_x.setEnabled(True) # Si se oculta (hide) el boton, re-habilitar el boton de close
            return
        r = self.rect_actual
        # Reducción escalonada (CRT horizontal)
        nuevo_alto = max(0, r.height() - (r.height() // self.pasos))
        nuevo_y = r.y() + (r.height() - nuevo_alto) // 2
        self.rect_actual = QRect(
            r.x(),      # Posición de x no cambia
            nuevo_y,    # Y centrado
            r.width(),  # Ancho no cambia
            nuevo_alto  # Altura disminuye
        )
        self.setGeometry(self.rect_actual)
        self.paso_actual += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
