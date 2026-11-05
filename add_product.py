
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QInputDialog, QMessageBox

def load_dropdown_items(field_name):
    try:  # Read items from text file and populate dropdown
        with open(f"drop_down_lists/{field_name}.txt", "r", encoding="utf-8") as file:
            items = [line.strip() for line in file if line.strip()]
            items.append(f"Add new {field_name}")
            return items
    except FileNotFoundError:
        print(f"Error: {field_name}.txt file not found.")
        items = [f"Error loading {field_name}"]
        return items

def add_to_dropdown(field_name,new_item):
    with open(f"drop_down_lists/{field_name}.txt", "r", encoding="utf-8") as file:
        items = [line.strip() for line in file if line.strip()]
    # check new_item is unique - yes: continue and return true, no: return error (false)
    items.append(new_item)
    items.sort()
    with open(f"drop_down_lists/{field_name}.txt", "w", encoding="utf-8") as file:
        file.writelines("\n".join(items))
    return True

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # product category
        self.label = QLabel("Product Category")
        self.category_dropdown = QComboBox()
        self.load_dropdown("category")
        layout.addWidget(self.label)
        layout.addWidget(self.category_dropdown)

        # Item Number (yarn)      Brand Name + Item Number (unique)
        # Barcode                 (unique)
        # Brand Name (yarn)     DD
        # Product Name
        # Discount (yarn)       Boolean
        # Taxable (yarn)        Boolean
        # Sold By (yarn)        DD

        # Unit (yarn - each)    DD
        # Weight of Unit (yarn - each)    DD?
        #  Line (yarn - each - weight)
        # Yarn Size (yarn - each - weight)      DD
        # Type (yarn - each - weight)
        # Fiber Type (yarn - each - weight)     DD
        # Color Number (yarn - each - weight)
        # Color (yarn - each - weight)

        # self.dev_label = QLabel("Preferred Programming Language:")
        # self.dev_input = QLineEdit()
        # layout.addWidget(self.dev_label)
        # layout.addWidget(self.dev_input)

        # self.update_field_visibility("")

        self.setLayout(layout)
        self.setWindowTitle("Dynamic Form")
        # self.resize(300, 200)

    def load_dropdown(self,list_name):
        items = load_dropdown_items(list_name)
        dropdown_name = list_name + '_dropdown'
        getattr(self, dropdown_name).addItems(items)
        getattr(self, dropdown_name).setPlaceholderText("")
        getattr(self, dropdown_name).setCurrentIndex(-1)
        getattr(self, dropdown_name).currentTextChanged.connect(self.on_change)

    def reload_dropdown(self,list_name,item):
        dropdown_name = list_name + '_dropdown'
        getattr(self, dropdown_name).clear()
        items = load_dropdown_items(list_name)
        getattr(self, dropdown_name).addItems(items)
        getattr(self, dropdown_name).setCurrentText(item)

    def on_change(self, selected_text):
        if "Add new" in selected_text:
            list_name = selected_text.split()[-1].lower()
            new_item = self.show_input_box(f"Add new {list_name}")
            if new_item != "":
                result = add_to_dropdown(list_name, new_item)
                # if add_to_dropdown returns "error" do same as else below
                self.reload_dropdown(list_name, new_item)
            else:
                dropdown_name = list_name + '_dropdown'
                getattr(self, dropdown_name).setPlaceholderText("")
                getattr(self, dropdown_name).setCurrentIndex(-1)
        # else:
        #     self.update_field_visibility(selected_text)
    #
    # def update_field_visibility(self, role):
    #     is_dev = (role == "Developer")
    #     self.dev_label.setVisible(is_dev)
    #     self.dev_input.setVisible(is_dev)
    #     self.adjustSize()

    def show_input_box(self,input_label):
        # QInputDialog.getText returns a tuple: (text_entered, ok_clicked)
        text, ok = QInputDialog.getText(
            self,
            "New Dropdown Item",  # Window title
            input_label  # Label text
        )
        # Check if the user clicked 'OK'
        if ok and text:
            # QMessageBox.information(self, "Success", f"Hello, {text}!")
            return text
        elif ok:
            QMessageBox.warning(self, "Warning", "You didn't enter anything!")
            return ""