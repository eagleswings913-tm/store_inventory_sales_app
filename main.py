
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
import sys
from add_product import MyWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
