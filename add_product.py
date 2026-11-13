
from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QInputDialog, QMessageBox, \
    QLineEdit, QPushButton, QFormLayout, QMainWindow, QHBoxLayout

import dropdown_menus
from window_functions import set_title_bar_color,center_on_cursor_screen

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        set_title_bar_color(self, 0xDC9570)  # 7095DC
        center_on_cursor_screen(self)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(40,20,40,20)
        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(0,20,0,20)

            # product category - category_dropdown
        self.category_label = QLabel("Product Category")
        self.category_dropdown = QComboBox()
        self.category_dropdown.setObjectName("category_dropdown")
        self.load_dropdown("category")
        self.form_layout.addRow(self.category_label, self.category_dropdown)

        self.category_index = QLineEdit()
        self.category_index.setObjectName("category_index")
        self.form_layout.addRow(self.category_index)
        self.category_index.setVisible(False)

        # Barcode                 (unique)
        self.barcode_label = QLabel("Barcode")
        self.barcode = QLineEdit()
        self.barcode.setObjectName("barcode")
        self.form_layout.addRow(self.barcode_label, self.barcode)
        self.barcode.returnPressed.connect(lambda w=self.barcode: self.on_change(w.text(),"barcode"))
        self.form_layout.setRowVisible(self.barcode, False)

        # Item Number (yarn)      Brand Name + Item Number (unique)
        self.item_num_label = QLabel("Item Number")
        self.item_num = QLineEdit()
        self.item_num.setObjectName("barcode")
        self.form_layout.addRow(self.item_num_label, self.item_num)
        self.form_layout.setRowVisible(self.item_num, False)

        # Brand Name (yarn)     DD
        self.brand_name_label = QLabel("Brand Name")
        self.brand_name_dropdown = QComboBox()
        self.brand_name_dropdown.setObjectName("brand_name_dropdown")
        self.load_dropdown("brand_name")
        self.form_layout.addRow(self.brand_name_label, self.brand_name_dropdown)

        self.brand_name_index = QLineEdit()
        self.brand_name_index.setObjectName("brand_name_index")
        self.form_layout.addRow(self.brand_name_index)
        self.brand_name_index.setVisible(False)

        # Product Name          DD
        self.product_name_label = QLabel("Product Name")
        self.product_name_dropdown = QComboBox()
        self.product_name_dropdown.setObjectName("product_name_dropdown")
        self.load_dropdown("product_name")
        self.form_layout.addRow(self.product_name_label, self.product_name_dropdown)

        self.product_name_index = QLineEdit()
        self.product_name_index.setObjectName("product_name_index")
        self.form_layout.addRow(self.product_name_index)
        self.product_name_index.setVisible(False)

        # Discount (yarn)       Boolean
        self.discount_label = QLabel("Discount?")
        self.discount_dropdown = QComboBox()
        self.discount_dropdown.setObjectName("discount_dropdown")
        self.discount_dropdown.addItems(["True", "False"])
        self.discount_dropdown.setPlaceholderText("")
        self.discount_dropdown.setCurrentIndex(-1)
        self.form_layout.addRow(self.discount_label, self.discount_dropdown)

        # Taxable (yarn)        Boolean
        self.taxable_label = QLabel("Taxable?")
        self.taxable_dropdown = QComboBox()
        self.taxable_dropdown.setObjectName("taxable_dropdown")
        self.taxable_dropdown.addItems(["True", "False"])
        self.taxable_dropdown.setPlaceholderText("") # dropdown initially is empty
        self.taxable_dropdown.setCurrentIndex(-1)
        self.form_layout.addRow(self.taxable_label, self.taxable_dropdown)

        # Sold By (yarn)        DD
        self.sold_by_label = QLabel("Sold By")
        self.sold_by_dropdown = QComboBox()
        self.sold_by_dropdown.setObjectName("sold_by_dropdown")
        self.sold_by_dropdown.addItems(["Each", "Weight"])
        self.sold_by_dropdown.setPlaceholderText("")  # dropdown initially is empty
        self.sold_by_dropdown.setCurrentIndex(-1)
        self.form_layout.addRow(self.sold_by_label, self.sold_by_dropdown)

        # Unit (yarn - each)    DD
        self.unit_label = QLabel("Unit")
        self.unit_dropdown = QComboBox()
        self.unit_dropdown.setObjectName("unit_dropdown")
        self.load_dropdown("unit")
        self.form_layout.addRow(self.unit_label, self.unit_dropdown)

        self.unit_index = QLineEdit()
        self.unit_index.setObjectName("unit_index")
        self.form_layout.addRow(self.unit_index)
        self.unit_index.setVisible(False)

        # Weight of Unit (yarn - each)
        self.weight_per_unit_label = QLabel("Weight Per Unit")
        self.weight_per_unit = QLineEdit()
        self.weight_per_unit.setObjectName("weight_per_unit")
        self.form_layout.addRow(self.weight_per_unit_label, self.weight_per_unit)

        #  Line (yarn - each - weight)
        self.yarn_line_label = QLabel("Yarn Line")
        self.yarn_line = QLineEdit()
        self.yarn_line.setObjectName("yarn_line")
        self.form_layout.addRow(self.yarn_line_label, self.yarn_line)

        # Yarn Size (yarn - each - weight)      DD
        self.yarn_size_label = QLabel("Yarn Size")
        self.yarn_size_dropdown = QComboBox()
        self.yarn_size_dropdown.setObjectName("yarn_size_dropdown")
        self.load_dropdown("yarn_size")
        self.form_layout.addRow(self.yarn_size_label, self.yarn_size_dropdown)

        self.yarn_size_index = QLineEdit()
        self.yarn_size_index.setObjectName("yarn_size_index")
        self.form_layout.addRow(self.yarn_size_index)
        self.yarn_size_index.setVisible(False)

        # Type (yarn - each - weight)
        self.type_label = QLabel("Yarn Type (mercanized, perle, etc")
        self.type = QLineEdit()
        self.type.setObjectName("type")
        self.form_layout.addRow(self.type_label, self.type)

        # Fiber Type (yarn - each - weight)     DD
        self.fiber_type_label = QLabel("Fiber Type")
        self.fiber_type_dropdown = QComboBox()
        self.fiber_type_dropdown.setObjectName("fiber_type_dropdown")
        self.load_dropdown("fiber_type")
        self.form_layout.addRow(self.fiber_type_label, self.fiber_type_dropdown)

        self.fiber_type_index = QLineEdit()
        self.fiber_type_index.setObjectName("fiber_type_index")
        self.form_layout.addRow(self.fiber_type_index)
        self.fiber_type_index.setVisible(False)

        # Color Number (yarn - each - weight)
        self.color_num_label = QLabel("Color Number")
        self.color_num = QLineEdit()
        self.color_num.setObjectName("color_num")
        self.form_layout.addRow(self.color_num_label, self.color_num)

        # Color (yarn - each - weight)
        self.color_label = QLabel("Yarn Color")
        self.color_dropdown = QComboBox()
        self.color_dropdown.setObjectName("color_dropdown")
        self.load_dropdown("color")
        self.form_layout.addRow(self.color_label, self.color_dropdown)

        self.color_index = QLineEdit()
        self.color_index.setObjectName("color_index")
        self.form_layout.addRow(self.color_index)
        self.color_index.setVisible(False)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addStretch()

        # End of Form Layout

        # Begin Button Layout

        button_layout = QHBoxLayout()
            # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.handle_submit)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.handle_reset)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.handle_cancel)

        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(button_layout)

        # End Button Layout

        self.setWindowTitle("Dynamic Form")
        # self.resize(300, 200)

        # load dropdown items for each dropdown field (list_name)
    def load_dropdown(self,list_name):
        items = dropdown_menus.load_dropdown_items(list_name)              # retrieve dropdown items from list_name_dropdown.csv
        dropdown_name = list_name + '_dropdown'             # create widget name from list_name
        getattr(self, dropdown_name).addItems(items)        # add dropdown items to widget
        getattr(self, dropdown_name).setPlaceholderText("") # dropdown initially is empty
        getattr(self, dropdown_name).setCurrentIndex(-1)
            # action when text changes in dropdown
        getattr(self, dropdown_name).currentTextChanged.connect(lambda text: self.on_change(text,dropdown_name))

        # reload the widget dropdown items after adding a new item to the list
    def reload_dropdown(self,list_name,item):
        dropdown_name = list_name + '_dropdown'             # create widget name from list_name
        getattr(self, dropdown_name).clear()                # clear current dropdown list
        items = dropdown_menus.load_dropdown_items(list_name)              # retrieve dropdown items from list_name_dropdown.csv
        getattr(self, dropdown_name).addItems(items)        # add dropdown items to widget
        getattr(self, dropdown_name).setCurrentText(item)   # choose new item as current choice

        # executes when text changes in a dropdown widget
    def on_change(self, selected_text, widget_name):
        # print(selected_text, widget_name)
        list_name = widget_name.rsplit('_',1)[0].lower()            # extract fieldname from widget name
        # print(f"list name = {list_name}")
        if "Add new" in selected_text:                              # add new item to dropdown list
            list_name = selected_text.split()[-1].lower()           # extract field name from selected text
            new_item = self.show_input_box(f"Add new {list_name}")  # ask user for the name of the new dropdown item
            if new_item != "":
                result = dropdown_menus.add_to_dropdown(list_name, new_item)       # add new item to dropdown list
                if result:      # True if successful, False if new_item already exists or add if unsuccessful
                    self.reload_dropdown(list_name, new_item)       # reload widget dropdown items
                    QMessageBox.information(self, "Success", f"{new_item} added to dropdown")
                else:
                    dropdown_name = list_name + '_dropdown'         # create widget name from list_name
                    getattr(self, dropdown_name).setPlaceholderText("")     # dropdown initially is empty
                    getattr(self, dropdown_name).setCurrentIndex(-1)
                    QMessageBox.warning(self, "Warning", f"{new_item} was not added to dropdown.\n{new_item} already exists in dropdown list.")
            else:       # no new item inputed, reset widget dropdown
                dropdown_name = list_name + '_dropdown'
                getattr(self, dropdown_name).setPlaceholderText("")
                getattr(self, dropdown_name).setCurrentIndex(-1)
                QMessageBox.warning(self, "Warning", f"No new {list_name} was added.\n{list_name} was blank!")
        elif selected_text != "":               # other actions
            if list_name in ['brand_name','category','color','fiber_type','product_name','unit','yarn_size']:
                index = dropdown_menus.retrieve_index_of_choice(list_name, selected_text)      # return index for item if one of these widgets
                getattr(self, list_name + '_index').setText(index)              # set index as value for hidden widget field
            if list_name == "category":
                if self.question_box("Does the product have a barcode? (y or n) "):
                    self.form_layout.setRowVisible(self.barcode, True)
                    self.activateWindow()
                    self.barcode.setFocus()
                else:
                    list_name = "barcode"
            if list_name == "barcode":
                if self.question_box("Does the product have a item number? (y or n) "):
                    self.form_layout.setRowVisible(self.item_num, True)
                    self.activateWindow()
                    self.item_num.setFocus()
                else:
                    list_name = "item_num"

    def show_input_box(self,input_label):
        text, ok = QInputDialog.getText(
            self,
            "New Dropdown Item",  # Window title
            input_label  # Label text
        )
        if ok and text:         # clicked 'ok' and text entered
            return text
        elif ok:                # clicked 'ok' and no text entered
            return ""
        elif not ok:            # clicked 'X' or cancel
            return ""
        else:
            return ""

    def question_box(self,question_label):
        reply = QMessageBox.question(self, "Question Box", question_label,QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False

    def handle_submit(self):
        category = self.category_dropdown.currentText()
        category_index = self.category_index.text()
        barcode = self.barcode.text()
        item_num = self.item_num.text()

        # Process the form data
        QMessageBox.information(self, "Submitted", f"Category {category} with Index {category_index}\nbarcode {barcode}\nitem number {item_num}")

    def handle_reset(self):
        for i in range(self.form_layout.count()):
            item = self.form_layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    # print(widget.objectName())
                    widget_name = widget.objectName()
                    if isinstance(widget, QComboBox):
                        getattr(self, widget_name).setPlaceholderText("")  # dropdown initially is empty
                        getattr(self, widget_name).setCurrentIndex(-1)
                    elif isinstance(widget, QLineEdit):
                        getattr(self, widget_name).setText("")

        QMessageBox.information(self, "Reset", f"Reset the form")


    def handle_cancel(self):
        QMessageBox.information(self, "Cancel", f"Canceled, Return to main window")
        self.close()

    def closeEvent(self, event):
        event.accept()