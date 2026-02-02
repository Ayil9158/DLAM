# Ventana que:
# * Se encoge a una sola linea vertical
# * No congela la IU
# * Sonido retro (8-bit-game-2.wav)
# * Cierre fluido (OutCubic)
# * Deshabilita el boton de cierre con banderas
# * Destruye la ventana (si close)

import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve, QUrl
from PyQt5.QtMultimedia import QSoundEffect

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Efecto pantalla videojuego")
        self.resize(400, 300)

        # Botón X
        self.boton_x = QPushButton("X", self)
        self.boton_x.setFixedSize(30, 30)
        self.boton_x.move(360, 10)
        self.boton_x.clicked.connect(self.efecto_apagado)
        self.close()

        # Sonido retro
        ruta = os.path.abspath("/ProgramasPropios/ORV/Menu_Direct/System/Sounds/8-bit-game-2.wav")
        # print(ruta, os.path.exists(ruta))
        self.sonido = QSoundEffect(self)
        self.sonido.setSource(QUrl.fromLocalFile(ruta))
        self.sonido.setVolume(0.5)

        self.efecto_activo = False  # Bandera

    def efecto_apagado(self):
        if self.efecto_activo:  # Evita ejecución doble
            return
        self.efecto_activo = True

        self.boton_x.setEnabled(False)

        rect = self.geometry()
        self.sonido.play()
        centro_x = rect.x() + rect.width() // 2
        centro_y = rect.y() + rect.height() // 2
        # Rectángulo final (solo colapsar vertical / CRT)
        rect_final = QRect(
            rect.x(),
            rect.y() + rect.height() // 2,
            rect.width(),
            0
        )

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(500)  # ms
        self.anim.setStartValue(rect)
        self.anim.setEndValue(rect_final)
        # self.anim.setEasingCurve(QEasingCurve.InQuad)
        self.anim.setEasingCurve(QEasingCurve.OutCubic) # Empieza rapido y frena suave al final

        self.anim.finished.connect(self.close)
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
