import csv

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QInputDialog, QMessageBox, \
    QLineEdit

    # Read items from text file and return items to populate dropdown
def load_dropdown_items(field_name):
    try:
        with open(f"drop_down_lists/{field_name}.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            items = [row[0].strip() for row in reader if row and len(row) > 1]
            items.append(f"Add new {field_name}")
            return items
    except FileNotFoundError:
        print(f"Error: {field_name}.txt file not found.")
        items = [f"Error loading {field_name}"]
        return items

    # add new dropdown item to chosen list
def add_to_dropdown(field_name,new_item):
    list_items = []
    list_indexes = []
    items = []
        # read current dropdown list from file
    with open(f"drop_down_lists/{field_name}.csv", "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for line in csv_reader:
            list_items.append(line[0])      # append item name
            list_indexes.append(line[1])    # append item index
            items.append(line)              # append [item_name, index]
        # check new_item is unique - yes: continue and return true, no: return error (false)
    if new_item not in list_items:
            # create index for new item
        items_length = len(items)
        new_idx = items_length + 1
        if new_idx < 10:
            new_index = f"00{str(new_idx)}"
        elif new_idx < 100:
            new_index = f"0{str(new_idx)}"
        else:
            new_index = f"{str(new_idx)}"
        new_item = [new_item, new_index]        # append [new_item, new_index] is all items list and sort
        items.append(new_item)
        items.sort()
            # write updated dropdown list to file
        with open(f"drop_down_lists/{field_name}.csv", "w", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\n")
            csv_writer.writerows(items)
            return True
    else:   # item already exists in the dropdown list
        print(f"{new_item} already exists")
        return False

# find item in field_name csv file and return its index
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

            # product category - category_dropdown
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

        # load dropdown items for each dropdown field (list_name)
    def load_dropdown(self,list_name):
        items = load_dropdown_items(list_name)              # retrieve dropdown items from list_name_dropdown.csv
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
        items = load_dropdown_items(list_name)              # retrieve dropdown items from list_name_dropdown.csv
        getattr(self, dropdown_name).addItems(items)        # add dropdown items to widget
        getattr(self, dropdown_name).setCurrentText(item)   # choose new item as current choice

        # executes when text changes in a dropdown widget
    def on_change(self, selected_text, widget_name):
        list_name = widget_name.rsplit('_',1)[0].lower()            # extract fieldname from widget name
        if "Add new" in selected_text:                              # add new item to dropdown list
            list_name = selected_text.split()[-1].lower()           # extract field name from selected text
            new_item = self.show_input_box(f"Add new {list_name}")  # ask user for the name of the new dropdown item
            if new_item != "":
                result = add_to_dropdown(list_name, new_item)       # add new item to dropdown list
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
                index = retrieve_index_of_choice(list_name, selected_text)      # return index for item if one of these widgets
                getattr(self, list_name + '_index').setText(index)              # set index as value for hidden widget field

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