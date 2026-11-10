
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QMainWindow, QPushButton
import sys
from add_product import MyWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.add_button = QPushButton("Add Product")
        self.add_button.clicked.connect(self.show_add_product)
        layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Edit Product")
        self.edit_button.clicked.connect(self.show_add_product)
        layout.addWidget(self.edit_button)

        self.setLayout(layout)
        self.setWindowTitle("Dynamic Form")

    def show_add_product(self):
        w = MyWindow()
        w.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
