import csv

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QInputDialog, QMessageBox, \
    QLineEdit


def load_dropdown_items(field_name):
    try:  # Read items from text file and populate dropdown
        with open(f"drop_down_lists/{field_name}.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            items = [row[0].strip() for row in reader if row and len(row) > 1]
            items.append(f"Add new {field_name}")
            return items
    except FileNotFoundError:
        print(f"Error: {field_name}.txt file not found.")
        items = [f"Error loading {field_name}"]
        return items

def add_to_dropdown(field_name,new_item):
    list_items = []
    list_indexes = []
    items = []
    with open(f"drop_down_lists/{field_name}.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            list_items.append(line[0])
            list_indexes.append(line[1])
            items.append(line)
    # check new_item is unique - yes: continue and return true, no: return error (false)
    if new_item not in list_items:
        items_length = len(items)
        new_idx = items_length + 1
        if new_idx < 10:
            new_index = f"00{str(new_idx)}"
        elif new_idx < 100:
            new_index = f"0{str(new_idx)}"
        else:
            new_index = f"{str(new_idx)}"
        new_item = [new_item, new_index]
        items.append(new_item)
        items.sort()
        with open(f"drop_down_lists/{field_name}.csv", "w", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
            csv_writer.writerows(items)
            return True
    else:
        print(f"{new_item} already exists")
        return False

def retrieve_index_of_choice(field_name, item):
    with open(f"drop_down_lists/{field_name}.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            if item == line[0]:
                return line[1]


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
        self.category_index = QLineEdit()
        self.category_index.setVisible(False)
        layout.addWidget(self.label)
        layout.addWidget(self.category_dropdown)
        layout.addWidget(self.category_index)


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
        getattr(self, dropdown_name).currentTextChanged.connect(lambda text: self.on_change(text,dropdown_name))

    def reload_dropdown(self,list_name,item):
        dropdown_name = list_name + '_dropdown'
        getattr(self, dropdown_name).clear()
        items = load_dropdown_items(list_name)
        getattr(self, dropdown_name).addItems(items)
        getattr(self, dropdown_name).setCurrentText(item)

    def on_change(self, selected_text, widget_name):
        list_name = widget_name.rsplit('_',1)[0].lower()
        if "Add new" in selected_text:
            list_name = selected_text.split()[-1].lower()
            new_item = self.show_input_box(f"Add new {list_name}")
            if new_item != "":
                result = add_to_dropdown(list_name, new_item)
                # if add_to_dropdown returns "error" do same as else below
                if result:
                    self.reload_dropdown(list_name, new_item)
                    QMessageBox.information(self, "Success", f"{new_item} added to dropdown")
                else:
                    dropdown_name = list_name + '_dropdown'
                    getattr(self, dropdown_name).setPlaceholderText("")
                    getattr(self, dropdown_name).setCurrentIndex(-1)
                    QMessageBox.warning(self, "Warning", f"{new_item} was not added to dropdown.\n{new_item} already exists in dropdown list.")
            else:
                dropdown_name = list_name + '_dropdown'
                getattr(self, dropdown_name).setPlaceholderText("")
                getattr(self, dropdown_name).setCurrentIndex(-1)
                QMessageBox.warning(self, "Warning", f"No new {list_name} was added.\n{list_name} was blank!")
        elif selected_text != "":
            if list_name in ['brand_name','category','color','fiber_type','product_name','unit','yarn_size']:
                index = retrieve_index_of_choice(list_name, selected_text)
                getattr(self, list_name + '_index').setText(index)

    def show_input_box(self,input_label):
        # QInputDialog.getText returns a tuple: (text_entered, ok_clicked)
        text, ok = QInputDialog.getText(
            self,
            "New Dropdown Item",  # Window title
            input_label  # Label text
        )
        # Check if the user clicked 'OK'
        if ok and text:
            return text
        elif ok:
            return ""
        elif not ok:
            return ""