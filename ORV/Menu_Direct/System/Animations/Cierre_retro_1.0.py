# Ventana que:
# * Se encoge a una linea vertical en el centro
# * No congela la IU
# * Cierre no tan fluido (InQuad)
# * Destruye la ventana (si close)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve

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

    def efecto_apagado(self):
        rect = self.geometry()

        centro_x = rect.x() + rect.width() // 2
        centro_y = rect.y() + rect.height() // 2

        # Rectángulo final (línea en el centro)
        rect_final = QRect(centro_x, centro_y, 0, 0)

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(500)  # ms
        self.anim.setStartValue(rect)
        self.anim.setEndValue(rect_final)
        self.anim.setEasingCurve(QEasingCurve.InQuad)

        self.anim.finished.connect(self.close)
        self.anim.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
