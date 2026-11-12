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
        self.set_title_bar_color(0xDC9570)     #7095DC
        # self.center_on_cursor_screen()
        self.setFixedSize(1200, 800)
        self.setStyleSheet("background-color: white")
        self.init_ui()

    def init_ui(self):
        grid_layout = QGridLayout(self)
        grid_layout.setContentsMargins(10, 10, 10, 10)
        grid_layout.setSpacing(10)
        grid_layout.setHorizontalSpacing(0)
        grid_layout.setVerticalSpacing(0)
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

        label1 = QLabel("")
        label1.setStyleSheet("background-color: #e1eaf9; border: 3px solid #b6caef;")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label1, 0, 1)

        label2 = QLabel("")
        label2.setStyleSheet("background-color: #e2eaf8; border: 3px solid #b6caef;")
        label2.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label2, 0, 2)

        grid_layout.setRowStretch(0, 1)

        label3 = QLabel("")
        label3.setStyleSheet("background-color: #e2eaf8; border: 3px solid #b6caef;")
        label3.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label3, 1, 1)

        label4 = QLabel("")
        label4.setStyleSheet("background-color: #e2eaf8; border: 3px solid #b6caef;")
        label4.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(label4, 1, 2)

        grid_layout.setRowStretch(1, 1)

        add_button = QLabel("")
        add_button.setStyleSheet("background-color: #e2eaf8; border: 3px solid #b6caef;")
        add_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(add_button, 2, 1)

        edit_button = QLabel("")
        edit_button.setStyleSheet("background-color: #e2eaf8; border: 3px solid #b6caef;")
        edit_button.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        grid_layout.addWidget(edit_button, 2, 2)

        grid_layout.setRowStretch(2, 1)

        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)
        grid_layout.setColumnStretch(2, 1)

        product_container = QWidget()
        product_container.setObjectName("ProductContainer")
        product_container.setStyleSheet("#ProductContainer {background-color: #e1eaf9; border: 3px solid #b6caef;}")
        product_container.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        product_grid = QGridLayout(product_container)
        product_label = QLabel("Products")
        product_label.setStyleSheet("border: none;")
        product_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        product_label.setStyleSheet("color: #7095DC;")
        product_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        product_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        product_grid.addWidget(product_label, 0, 0)
        product_grid.setRowStretch(0, 1)

        product_add_btn = QPushButton("Add Product")
        product_add_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        product_add_btn.setStyleSheet("color: #7095DC;")
        product_add_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        product_add_btn.clicked.connect(self.show_add_product)
        product_grid.addWidget(product_add_btn, 1, 0)
        product_grid.setRowStretch(1, 1)

        product_edit_btn = QPushButton("Edit Product")
        product_edit_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        product_edit_btn.setStyleSheet("color: #7095DC;")
        product_edit_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        product_grid.addWidget(product_edit_btn, 2, 0)
        product_grid.setRowStretch(2, 1)

        product_view_btn = QPushButton("View Product")
        product_view_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        product_view_btn.setStyleSheet("color: #7095DC;")
        product_view_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        product_grid.addWidget(product_view_btn, 3, 0)
        product_grid.setRowStretch(3, 1)

        grid_layout.addWidget(product_container, 0, 1)

        inventory_container = QWidget()
        inventory_container.setObjectName("InventoryContainer")
        inventory_container.setStyleSheet("#InventoryContainer {background-color: #e1eaf9; border: 3px solid #b6caef;}")
        inventory_container.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        inventory_grid = QGridLayout(inventory_container)
        inventory_label = QLabel("Inventory")
        inventory_label.setStyleSheet("border: none;")
        inventory_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        inventory_label.setStyleSheet("color: #7095DC;")
        inventory_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inventory_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        inventory_grid.addWidget(inventory_label, 0, 0)
        inventory_grid.setRowStretch(0, 1)

        inventory_add_btn = QPushButton("Add Inventory")
        inventory_add_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        inventory_add_btn.setStyleSheet("color: #7095DC;")
        inventory_add_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        inventory_add_btn.clicked.connect(self.show_add_product)
        inventory_grid.addWidget(inventory_add_btn, 1, 0)
        inventory_grid.setRowStretch(1, 1)

        inventory_edit_btn = QPushButton("Edit Inventory")
        inventory_edit_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        inventory_edit_btn.setStyleSheet("color: #7095DC;")
        inventory_edit_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        inventory_grid.addWidget(inventory_edit_btn, 2, 0)
        inventory_grid.setRowStretch(2, 1)

        inventory_view_btn = QPushButton("View Inventory")
        inventory_view_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        inventory_view_btn.setStyleSheet("color: #7095DC;")
        inventory_view_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        inventory_grid.addWidget(inventory_view_btn, 3, 0)
        inventory_grid.setRowStretch(3, 1)

        grid_layout.addWidget(inventory_container, 0, 2)

        sales_container = QWidget()
        sales_container.setObjectName("SalesContainer")
        sales_container.setStyleSheet("#SalesContainer {background-color: #e1eaf9; border: 3px solid #b6caef;}")
        sales_container.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sales_grid = QGridLayout(sales_container)
        sales_label = QLabel("Sales")
        sales_label.setStyleSheet("border: none;")
        sales_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        sales_label.setStyleSheet("color: #7095DC;")
        sales_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sales_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sales_grid.addWidget(sales_label, 0, 0)
        sales_grid.setRowStretch(0, 1)

        sales_add_btn = QPushButton("Add Sale")
        sales_add_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        sales_add_btn.setStyleSheet("color: #7095DC;")
        sales_add_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sales_add_btn.clicked.connect(self.show_add_product)
        sales_grid.addWidget(sales_add_btn, 1, 0)
        sales_grid.setRowStretch(1, 1)

        sales_edit_btn = QPushButton("Edit Sale")
        sales_edit_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        sales_edit_btn.setStyleSheet("color: #7095DC;")
        sales_edit_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sales_grid.addWidget(sales_edit_btn, 2, 0)
        sales_grid.setRowStretch(2, 1)

        sales_view_btn = QPushButton("View Sales")
        sales_view_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        sales_view_btn.setStyleSheet("color: #7095DC;")
        sales_view_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sales_grid.addWidget(sales_view_btn, 3, 0)
        sales_grid.setRowStretch(3, 1)

        grid_layout.addWidget(sales_container, 1, 1)

        reports_container = QWidget()
        reports_container.setObjectName("ReportsContainer")
        reports_container.setStyleSheet("#ReportsContainer {background-color: #e1eaf9; border: 3px solid #b6caef;}")
        reports_container.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        reports_grid = QGridLayout(reports_container)
        reports_label = QLabel("Reports")
        reports_label.setStyleSheet("border: none;")
        reports_label.setFont(QFont("Arial", 30, QFont.Weight.Bold))
        reports_label.setStyleSheet("color: #7095DC;")
        reports_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        reports_label.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        reports_grid.addWidget(reports_label, 0, 0)
        reports_grid.setRowStretch(0, 1)

        reports_view_btn = QPushButton("View Reports")
        reports_view_btn.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        reports_view_btn.setStyleSheet("color: #7095DC;")
        reports_view_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        reports_grid.addWidget(reports_view_btn, 1, 0)
        reports_grid.setRowStretch(1, 1)

        grid_layout.addWidget(reports_container, 1, 2)

        # if grid_layout:
        #     for row in range(grid_layout.rowCount()):
        #         for col in range(grid_layout.columnCount()):
        #             item = grid_layout.itemAtPosition(row, col)
        #             if item is not None and item.widget() is not None:
        #                 size = item.widget().size()
        #                 print(
        #                     f"Widget at ({row}, {col}) -> Width: {size.width()}, Height:"
        #                     f" {size.height()}"
        #                 )

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
