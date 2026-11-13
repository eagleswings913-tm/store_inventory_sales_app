from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel

class DigitalClock(QLabel):

  def __init__(self, parent=None):
    super().__init__(parent)
    self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    self.setFont(QFont("Arial", 24, QFont.Weight.Bold))
    self.setStyleSheet("color: #7095DC;")

    # Set up a timer to trigger every 1000ms (1 second)
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_time)
    self.timer.start(1000)

    # Display the time immediately on startup
    self.update_time()

  def update_time(self):
    current_time = QTime.currentTime().toString("hh:mm:ss AP")
    self.setText(current_time)