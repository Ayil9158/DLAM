# Ventana que:
# * Parpadea cada 0.5 segundos durante 10 segundos
# * No congela la IU
# * No destruye la ventana (no close)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QTimer

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parpadeo con QTimer")
        self.resize(400, 300)

        # Botón "X"
        self.boton_x = QPushButton("X", self)
        self.boton_x.setFixedSize(30, 30)
        self.boton_x.move(360, 10)  # esquina superior derecha
        self.boton_x.clicked.connect(self.iniciar_parpadeo)

        # Timer para parpadeo
        self.timer_parpadeo = QTimer(self)
        self.timer_parpadeo.timeout.connect(self.toggle_visibilidad)
        
        # Timer para detener a los 5 seg
        self.timer_fin = QTimer(self)
        self.timer_fin.setSingleShot(True)
        self.timer_fin.timeout.connect(self.detener_parpadeo)

    def iniciar_parpadeo(self):
        self.timer_parpadeo.start(500)
        self.timer_fin.start(10000)

    def toggle_visibilidad(self):
        self.setVisible(not self.isVisible())
        
    def detener_parpadeo(self):
        self.timer_parpadeo.stop()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
