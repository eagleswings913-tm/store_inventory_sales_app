import ctypes
from datetime import date

from PySide6.QtCore import Qt, QTimer, QTime
from PySide6.QtGui import QPixmap, QCursor, QGuiApplication, QFont
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QMainWindow, QPushButton, \
    QGridLayout, QSizePolicy
import sys
from add_product import MyWindow

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

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A Place to Weave")
        self.set_title_bar_color(0xE6C29B)
        self.center_on_cursor_screen()
        self.setFixedSize(1200, 800)
        self.setStyleSheet("background-color: white")
        self.init_ui()

    def init_ui(self):
        grid_layout = QGridLayout(self)
        grid_layout.setContentsMargins(10, 10, 10, 10)
        grid_layout.setSpacing(10)
        self.setLayout(grid_layout)

        image_label = QLabel("Image Placeholder")
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pixmap = QPixmap("images/logo_resized.png")
        if not pixmap.isNull():
            image_label.setPixmap(
                pixmap.scaled(
                    320,
                    480,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        # Signature: addWidget(widget, row, column, rowSpan, columnSpan)
        grid_layout.addWidget(image_label, 0, 0, 2, 1)

        date_time_grid = QGridLayout()
        day = date.today().strftime("%A")
        day_label = QLabel(f"{day}")
        day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        day_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        day_label.setStyleSheet("color: #7095DC;")
        date_time_grid.addWidget(day_label, 0, 0)
        self.clock = DigitalClock(self)
        date_time_grid.addWidget(self.clock, 2, 0)
        today_mmddyyyy = date.today().strftime("%m/%d/%Y")
        date_time_label = QLabel(f"{today_mmddyyyy}")
        date_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        date_time_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        date_time_label.setStyleSheet("color: #7095DC;")
        date_time_grid.addWidget(date_time_label, 1, 0)
        grid_layout.addLayout(date_time_grid, 2, 0)

        label1 = QPushButton("red")
        label1.setStyleSheet("background-color: red; border: 1px solid black")
        label1.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label1, 0, 1)

        label2 = QPushButton("orange")
        label2.setStyleSheet("background-color: orange")
        label2.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label2, 0, 2)

        grid_layout.setRowStretch(0, 1)

        label3 = QPushButton("yellow")
        label3.setStyleSheet("background-color: yellow")
        label3.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label3, 1, 1)

        label4 = QPushButton("green")
        label4.setStyleSheet("background-color: green")
        label4.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label4, 1, 2)

        grid_layout.setRowStretch(1, 1)

        add_button = QPushButton("blue")
        add_button.setStyleSheet("background-color: blue")
        add_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(add_button, 2, 1)

        edit_button = QPushButton("purple")
        edit_button.setStyleSheet("background-color: purple")
        edit_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(edit_button, 2, 2)

        grid_layout.setRowStretch(2, 1)

        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 1)

        if grid_layout:
            for row in range(grid_layout.rowCount()):
                for col in range(grid_layout.columnCount()):
                    item = grid_layout.itemAtPosition(row, col)
                    if item is not None and item.widget() is not None:
                        size = item.widget().size()
                        print(
                            f"Widget at ({row}, {col}) -> Width: {size.width()}, Height:"
                            f" {size.height()}"
                        )

    def center_on_cursor_screen(self):
        # Find the screen where the mouse cursor is currently located
        cursor_pos = QCursor.pos()
        target_screen = QGuiApplication.screenAt(cursor_pos)

        # Fallback to the primary screen if the cursor position isn't detected
        if target_screen is None:
            target_screen = QGuiApplication.primaryScreen()

        # Calculate and apply the center position
        screen_center = target_screen.availableGeometry().center()
        window_rect = self.frameGeometry()
        window_rect.moveCenter(screen_center)
        self.move(window_rect.topLeft())

    def set_title_bar_color(self, bgr_color: int):
        if sys.platform == "win32":
            hwnd = int(self.winId())
            # DWMWA_CAPTION_COLOR = 35 (Windows 11 Build 22000+)
            DWMWA_CAPTION_COLOR = 35
            color = ctypes.c_int(bgr_color)
            ctypes.windll.dwmapi.DwmSetWindowAttribute(
                hwnd,
                DWMWA_CAPTION_COLOR,
                ctypes.byref(color),
                ctypes.sizeof(color)
            )

    def show_add_product(self):
        w = MyWindow()
        w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
