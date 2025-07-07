from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPainterPath, QPen, QColor, QPalette
from PyQt5.QtCore import Qt

class FancyContainer1(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        paint_path = QPainterPath()
        paint_path.moveTo(0, 30) # Top left corner
        paint_path.lineTo(30, 0)
        paint_path.lineTo(width - 10, 0) # Top right corner
        paint_path.lineTo(width, 10)
        paint_path.lineTo(width, height - 20) # Bottom right corner
        paint_path.lineTo(width - 20, height)
        paint_path.lineTo(10, height) # Bottom left corner
        paint_path.lineTo(0, height - 10)
        paint_path.closeSubpath()

        bg_color = self.palette().window() # Take the background color defined in QSS
        border_color = self.palette().color(QPalette.WindowText) # White
        # Outer line
        outer_pen = QPen(border_color, 6)
        painter.setPen(outer_pen)
        painter.drawPath(paint_path)
        # Middle line
        middle_pen = QPen(bg_color, 2)
        painter.setPen(middle_pen)
        painter.drawPath(paint_path)
        # Inner line
        inner_pen = QPen(border_color,1)
        painter.setPen(inner_pen)
        painter.drawPath(paint_path)

        painter.fillPath(paint_path, bg_color)



class FancyContainer2(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        paint_path = QPainterPath()
        paint_path.moveTo(0, 30)
        paint_path.lineTo(30, 0)
        paint_path.lineTo(width - 10, 0)
        paint_path.lineTo(width, 10)
        paint_path.lineTo(width, height)
        paint_path.lineTo(0, height)
        paint_path.closeSubpath()

        bg_color = self.palette().window() # Take the background color defined in QSS
        border_color = self.palette().color(QPalette.WindowText) # White
        # Outer line
        outer_pen = QPen(border_color, 6)
        painter.setPen(outer_pen)
        painter.drawPath(paint_path)
        # Middle line
        middle_pen = QPen(bg_color, 2)
        painter.setPen(middle_pen)
        painter.drawPath(paint_path)
        # Inner line
        inner_pen = QPen(border_color,1)
        painter.setPen(inner_pen)
        painter.drawPath(paint_path)

        painter.fillPath(paint_path, bg_color)