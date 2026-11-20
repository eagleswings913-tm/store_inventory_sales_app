from PySide6.QtCore import Signal, QTimer, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QInputDialog, QMessageBox, \
    QLineEdit, QPushButton, QFormLayout, QMainWindow, QHBoxLayout

import dropdown_menus
from window_functions import set_title_bar_color,center_on_cursor_screen

class MyWindow(QMainWindow):
    form_submitted = Signal(dict)
    def __init__(self):
        super().__init__()
        set_title_bar_color(self, 0xDC9570)  # 7095DC
        center_on_cursor_screen(self)
        self.reset = False
        self.PRODUCT_REQUIRED_FIELDS = ['category','barcode','item_num','brand_name','product_name','discount','taxable']
        self.YARN_EACH_REQUIRED_FIELDS = ['category','brand_name','sold_by','discount','taxable','yarn_size','fiber_type','color_num','color','unit','weight_per_unit']
        self.YARN_WEIGHT_REQUIRED_FIELDS = ['category','brand_name','sold_by','discount','taxable','yarn_size','fiber_type','color_num','color']
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(40,20,40,20)
        self.form_layout = QFormLayout()
        self.form_layout.setContentsMargins(0,20,0,20)

            # message label
        self.message_label = QLabel("Message Goes Here")
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.message_label.setStyleSheet("color: #dc70b9; background-color: #b6caef")
        self.message_label.setObjectName("message")
        self.form_layout.addRow(self.message_label)
        self.message_label.setVisible(False)

            # product category - category_dropdown
        self.category_label = QLabel("<b>Product Category</b> - <span style='color:red;'>Required</span>")
        self.category_dropdown = QComboBox()
        self.category_dropdown.setObjectName("category_dropdown")
        self.load_dropdown("category")
        self.form_layout.addRow(self.category_label, self.category_dropdown)

        self.category_index = QLineEdit()
        self.category_index.setObjectName("category_index")
        self.form_layout.addRow(self.category_index)
        self.category_index.setVisible(False)

        # Barcode                 (unique)
        self.barcode_label = QLabel("<b>Barcode</b>")
        self.barcode = QLineEdit()
        self.barcode.setObjectName("barcode")
        self.form_layout.addRow(self.barcode_label, self.barcode)
        self.barcode.returnPressed.connect(lambda w=self.barcode: self.on_change(w.text(),"barcode"))
        self.form_layout.setRowVisible(self.barcode, False)

        # Item Number (yarn)      Brand Name + Item Number (unique)
        self.item_num_label = QLabel("<b>Item Number</b> - <span style='color:red;'>Required</span>")
        self.item_num = QLineEdit()
        self.item_num.setObjectName("item_num")
        self.form_layout.addRow(self.item_num_label, self.item_num)
        self.item_num.returnPressed.connect(lambda w=self.item_num: self.on_change(w.text(), "item_num"))
        self.form_layout.setRowVisible(self.item_num, False)

        # Sold By (yarn)        DD
        self.sold_by_label = QLabel("<b>Sold By</b> - <span style='color:red;'>Required</span>")
        self.sold_by_dropdown = QComboBox()
        self.sold_by_dropdown.setObjectName("sold_by_dropdown")
        self.sold_by_dropdown.addItems(["Each", "Weight"])
        self.sold_by_dropdown.setPlaceholderText("")  # dropdown initially is empty
        self.sold_by_dropdown.setCurrentIndex(-1)
        self.form_layout.addRow(self.sold_by_label, self.sold_by_dropdown)
        self.sold_by_dropdown.currentTextChanged.connect(lambda text: self.on_change(text,'sold_by_dropdown'))
        self.form_layout.setRowVisible(self.sold_by_dropdown, False)

        # Brand Name (yarn)     DD
        self.brand_name_label = QLabel("<b>Brand Name</b> - <span style='color:red;'>Required</span>")
        self.brand_name_dropdown = QComboBox()
        self.brand_name_dropdown.setObjectName("brand_name_dropdown")
        self.load_dropdown("brand_name")
        self.form_layout.addRow(self.brand_name_label, self.brand_name_dropdown)
        self.form_layout.setRowVisible(self.brand_name_dropdown, False)

        self.brand_name_index = QLineEdit()
        self.brand_name_index.setObjectName("brand_name_index")
        self.form_layout.addRow(self.brand_name_index)
        self.brand_name_index.setVisible(False)

        # Product Name          DD
        self.product_name_label = QLabel("<b>Product Name</b> - <span style='color:red;'>Required</span>")
        self.product_name_dropdown = QComboBox()
        self.product_name_dropdown.setObjectName("product_name_dropdown")
        self.load_dropdown("product_name")
        self.form_layout.addRow(self.product_name_label, self.product_name_dropdown)
        self.form_layout.setRowVisible(self.product_name_dropdown, False)

        self.product_name_index = QLineEdit()
        self.product_name_index.setObjectName("product_name_index")
        self.form_layout.addRow(self.product_name_index)
        self.product_name_index.setVisible(False)

        # Discount (yarn)       Boolean
        self.discount_label = QLabel("<b>Discount?</b> - <span style='color:red;'>Required</span>")
        self.discount_dropdown = QComboBox()
        self.discount_dropdown.setObjectName("discount_dropdown")
        self.discount_dropdown.addItems(["True", "False"])
        self.discount_dropdown.setPlaceholderText("")
        self.discount_dropdown.setCurrentIndex(-1)
        self.form_layout.addRow(self.discount_label, self.discount_dropdown)
        self.discount_dropdown.currentTextChanged.connect(lambda text: self.on_change(text,'discount_dropdown'))
        self.form_layout.setRowVisible(self.discount_dropdown, False)

        # Taxable (yarn)        Boolean
        self.taxable_label = QLabel("<b>Taxable?</b> - <span style='color:red;'>Required</span>")
        self.taxable_dropdown = QComboBox()
        self.taxable_dropdown.setObjectName("taxable_dropdown")
        self.taxable_dropdown.addItems(["True", "False"])
        self.taxable_dropdown.setPlaceholderText("") # dropdown initially is empty
        self.taxable_dropdown.setCurrentIndex(-1)
        self.form_layout.addRow(self.taxable_label, self.taxable_dropdown)
        self.taxable_dropdown.currentTextChanged.connect(lambda text: self.on_change(text,'taxable_dropdown'))
        self.form_layout.setRowVisible(self.taxable_dropdown, False)

        # Yarn Size (yarn - each - weight)      DD
        self.yarn_size_label = QLabel("<b>Yarn Size</b> - <span style='color:red;'>Required</span>")
        self.yarn_size_dropdown = QComboBox()
        self.yarn_size_dropdown.setObjectName("yarn_size_dropdown")
        self.load_dropdown("yarn_size")
        self.form_layout.addRow(self.yarn_size_label, self.yarn_size_dropdown)
        self.form_layout.setRowVisible(self.yarn_size_dropdown, False)

        self.yarn_size_index = QLineEdit()
        self.yarn_size_index.setObjectName("yarn_size_index")
        self.form_layout.addRow(self.yarn_size_index)
        self.yarn_size_index.setVisible(False)

        # Fiber Type (yarn - each - weight)     DD
        self.fiber_type_label = QLabel("<b>Fiber Type</b> - <span style='color:red;'>Required</span>")
        self.fiber_type_dropdown = QComboBox()
        self.fiber_type_dropdown.setObjectName("fiber_type_dropdown")
        self.load_dropdown("fiber_type")
        self.form_layout.addRow(self.fiber_type_label, self.fiber_type_dropdown)
        self.form_layout.setRowVisible(self.fiber_type_dropdown, False)

        self.fiber_type_index = QLineEdit()
        self.fiber_type_index.setObjectName("fiber_type_index")
        self.form_layout.addRow(self.fiber_type_index)
        self.fiber_type_index.setVisible(False)

        # Color Number (yarn - each - weight)
        self.color_num_label = QLabel("<b>Color Number</b> - <span style='color:red;'>Required</span>")
        self.color_num = QLineEdit()
        self.color_num.setObjectName("color_num")
        self.form_layout.addRow(self.color_num_label, self.color_num)
        self.form_layout.setRowVisible(self.color_num, False)

        # Color (yarn - each - weight)
        self.color_label = QLabel("<b>Yarn Color</b> - <span style='color:red;'>Required</span>")
        self.color_dropdown = QComboBox()
        self.color_dropdown.setObjectName("color_dropdown")
        self.load_dropdown("color")
        self.form_layout.addRow(self.color_label, self.color_dropdown)
        self.form_layout.setRowVisible(self.color_dropdown, False)

        self.color_index = QLineEdit()
        self.color_index.setObjectName("color_index")
        self.form_layout.addRow(self.color_index)
        self.color_index.setVisible(False)

        #  Line (yarn - each - weight)
        self.yarn_line_label = QLabel("<b>Yarn Line</b>")
        self.yarn_line = QLineEdit()
        self.yarn_line.setObjectName("yarn_line")
        self.form_layout.addRow(self.yarn_line_label, self.yarn_line)
        self.form_layout.setRowVisible(self.yarn_line, False)

        # Type (yarn - each - weight)
        self.type_label = QLabel("<b>Yarn Type</b> (mercanized, perle, etc")
        self.type = QLineEdit()
        self.type.setObjectName("type")
        self.form_layout.addRow(self.type_label, self.type)
        self.form_layout.setRowVisible(self.type, False)

        # Unit (yarn - each)    DD
        self.unit_label = QLabel("<b>Unit</b> - <span style='color:red;'>Required</span>")
        self.unit_dropdown = QComboBox()
        self.unit_dropdown.setObjectName("unit_dropdown")
        self.load_dropdown("unit")
        self.form_layout.addRow(self.unit_label, self.unit_dropdown)
        self.form_layout.setRowVisible(self.unit_dropdown, False)

        self.unit_index = QLineEdit()
        self.unit_index.setObjectName("unit_index")
        self.form_layout.addRow(self.unit_index)
        self.unit_index.setVisible(False)

        # Weight of Unit (yarn - each)
        self.weight_per_unit_label = QLabel("<b>Weight Per Unit</b> - <span style='color:red;'>Required</span>")
        self.weight_per_unit = QLineEdit()
        self.weight_per_unit.setObjectName("weight_per_unit")
        self.form_layout.addRow(self.weight_per_unit_label, self.weight_per_unit)
        self.form_layout.setRowVisible(self.weight_per_unit, False)

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
        if self.reset:
            return
        if 'dropdown' in widget_name:
            list_name = widget_name.rsplit('_',1)[0].lower()            # extract fieldname from widget name
        else:
            list_name = widget_name
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
            self.message_label.setText("")
            self.message_label.setVisible(False)
            QTimer.singleShot(0, self.adjustSize)
            if self.question_box("Does the product have a barcode? (y or n) "):
                self.form_layout.setRowVisible(self.barcode, True)
                self.activateWindow()
                self.barcode.setFocus()
            else:
                list_name = 'barcode'
        if list_name == "barcode":
            category = self.category_dropdown.currentText()
            if category != 'yarn':
                self.form_layout.setRowVisible(self.item_num, True)
                self.form_layout.setRowVisible(self.brand_name_dropdown, True)
                self.form_layout.setRowVisible(self.product_name_dropdown, True)
                self.form_layout.setRowVisible(self.discount_dropdown, True)
                self.form_layout.setRowVisible(self.taxable_dropdown, True)
                self.focusNextChild()
            else:
                if self.question_box("Does the product have an Item number? (y or n) "):
                    self.form_layout.setRowVisible(self.item_num, True)
                    self.item_num.setFocus()
                else:
                    list_name = 'item_num'
        if list_name == "item_num":
            category = self.category_dropdown.currentText()
            if category == 'yarn':
                self.form_layout.setRowVisible(self.sold_by_dropdown, True)
            self.item_num.clearFocus()
        if list_name == "sold_by":
            self.message_label.setText("")
            self.message_label.setVisible(False)
            self.form_layout.setRowVisible(self.brand_name_dropdown, True)
            self.form_layout.setRowVisible(self.discount_dropdown, True)
            self.form_layout.setRowVisible(self.taxable_dropdown, True)
            self.form_layout.setRowVisible(self.yarn_size_dropdown, True)
            self.form_layout.setRowVisible(self.fiber_type_dropdown, True)
            self.form_layout.setRowVisible(self.color_num, True)
            self.form_layout.setRowVisible(self.color_dropdown, True)
            self.form_layout.setRowVisible(self.yarn_line, True)
            self.form_layout.setRowVisible(self.type, True)
            if selected_text == "Each":
                self.form_layout.setRowVisible(self.unit_dropdown, True)
                self.form_layout.setRowVisible(self.weight_per_unit, True)

        if list_name == "brand_name":
            self.focusNextChild()
        if list_name == "product_name":
            self.focusNextChild()
        if list_name == "discount_name":
            self.focusNextChild()
        if list_name == "taxable":
            self.focusNextChild()

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

    def is_empty(self, field_name, field_value):
        print(f"category = {self.category_dropdown.currentText()} | sold by = {self.sold_by_dropdown.currentText()} | field_name = {field_name} | field_value = {field_value}")
        if self.category_dropdown.currentText() != 'yarn' and field_name in self.PRODUCT_REQUIRED_FIELDS:
            if field_name == 'barcode' or field_name == 'item_num':
                if self.barcode.text() == "" and self.item_num.text() == "":
                    self.message_label.setText("Barcode and Item number can NOT both be empty!!!!!")
                    self.message_label.setVisible(True)
                    self.form_layout.setRowVisible(self.barcode, True)
                    return False
            else:
                if field_value == '':
                    self.message_label.setText(f"{field_name} is a required field")
                    self.message_label.setVisible(True)
                    return False
        elif self.category_dropdown.currentText() == 'yarn' and self.sold_by_dropdown.currentText() == 'Weight' and field_name in self.YARN_WEIGHT_REQUIRED_FIELDS:
            if field_value == '':
                self.message_label.setText(f"{field_name} is a required field")
                self.message_label.setVisible(True)
                return False
        elif self.category_dropdown.currentText() == 'yarn' and self.sold_by_dropdown.currentText() == 'Each' and field_name in self.YARN_EACH_REQUIRED_FIELDS:
            if field_value == '':
                self.message_label.setText(f"{field_name} is a required field")
                self.message_label.setVisible(True)
                return False
        elif field_name == 'sold_by' and self.sold_by_dropdown.currentText() == '':
            self.message_label.setText(f"{field_name} is a required field")
            self.message_label.setVisible(True)
            return False

        return True

    def validate_fields(self):
        self.message_label.setText("")
        self.message_label.setVisible(False)
        for i in range(self.form_layout.count()):
            item = self.form_layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    # print(widget.objectName())
                    widget_name = widget.objectName()
                    # print(f"widget = {widget_name}")
                    if isinstance(widget, QComboBox):
                        widget_value = getattr(self, widget_name).currentText()
                        field_name = widget_name.rsplit('_',1)[0].lower()
                        # print(f"widget = {widget_name} | field name = {field_name} | widget_value = {widget_value}")
                        if not self.is_empty(field_name,widget_value):
                            return False
                    elif isinstance(widget, QLineEdit):
                        widget_value = getattr(self, widget_name).text()
                        field_name = widget_name
                        # print(f"widget = {widget_name} | field name = {field_name} | widget_value = {widget_value}")
                        if not self.is_empty(field_name,widget_value):
                            return False
        return True

    def handle_submit(self):
        if self.validate_fields():
            for i in range(self.form_layout.count()):
                item = self.form_layout.itemAt(i)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        # print(widget.objectName())
                        widget_name = widget.objectName()
                        # print(f"widget = {widget_name}")
                        if isinstance(widget, QComboBox):
                            widget_value = getattr(self, widget_name).currentText()
                            # print(f"widget = {widget_name} | widget_value = {widget_value}")
                        elif isinstance(widget, QLineEdit):
                            widget_value = getattr(self, widget_name).text()
                            # print(f"widget = {widget_name} | widget_value = {widget_value}")
            category = self.category_dropdown.currentText()
            category_index = self.category_index.text()
            barcode = self.barcode.text()
            item_num = self.item_num.text()
            brand_name = self.brand_name_dropdown.currentText()
            brand_name_index = self.brand_name_index.text()
            product_name = self.product_name_dropdown.currentText()
            product_name_index = self.product_name_index.text()
            discount = self.discount_dropdown.currentText()
            taxable = self.taxable_dropdown.currentText()
            sold_by = self.sold_by_dropdown.currentText()
            unit = self.unit_dropdown.currentText()
            unit_index = self.unit_index.text()
            weight_per_unit = self.weight_per_unit.text()
            yarn_line = self.yarn_line.text()
            yarn_size = self.yarn_size_dropdown.currentText()
            yarn_size_index = self.yarn_size_index.text()
            yarn_type = self.type.text()
            fiber_type = self.fiber_type_dropdown.currentText()
            fiber_type_index = self.fiber_type_index.text()
            color_num = self.color_num.text()
            color = self.color_dropdown.currentText()
            color_index = self.color_index.text()

            if category == 'yarn':
                if barcode == '':
                    barcode = f"{brand_name_index}{yarn_size_index}{fiber_type_index}{color_num}"
                    print(barcode)
                product_id = f"{brand_name} {yarn_size} {yarn_type} {fiber_type} {color}"
                print(product_id)
            else:
                if barcode == '':
                    barcode = f"{brand_name_index}{item_num}{product_name_index}"
                    print(barcode)
                product_id = f"{brand_name} {item_num} {product_name}"
                print(product_id)
            data = {
                "barcode": barcode,
                "product_id": product_id,
            }
            self.form_submitted.emit(data)

            # Process the form data
            QMessageBox.information(self, "Submitted", f"Category {category} with Index {category_index}\nbarcode {barcode}\nitem number {item_num}\nbrand name {brand_name} with index {brand_name_index}\nProduct name {product_name} with index {product_name_index}\nDiscount {discount}\nTaxable {taxable}\nSold By {sold_by}\nUnit {unit} with index {unit_index}\nweight per unit {weight_per_unit}\nyarn line {yarn_line}\nyarn size {yarn_size} with index {yarn_size_index}\ntype {yarn_type}\nfiber type {fiber_type} with index {fiber_type_index}\ncolor number {color_num}\nColor {color} with index {color_index}")

    def handle_reset(self):
        self.reset = True
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
                        if widget_name != "category_dropdown":
                            target_widget = getattr(self, widget_name)
                            self.form_layout.setRowVisible(target_widget, False)
                    elif isinstance(widget, QLineEdit):
                        getattr(self, widget_name).setText("")
                        target_widget = getattr(self, widget_name)
                        self.form_layout.setRowVisible(target_widget, False)
                        getattr(self, widget_name).setVisible(False)
        self.reset = False
        QTimer.singleShot(0, self.adjustSize)
        QMessageBox.information(self, "Reset", f"Reset the form")


    def handle_cancel(self):
        QMessageBox.information(self, "Cancel", f"Canceled, Return to main window")
        self.close()

    def closeEvent(self, event):
        event.accept()