
from add_product import MyWindow

def show_add_product():
    w = MyWindow()
    w.form_submitted.connect(process_form_data)
    w.show()

def process_form_data(data):
    print("Received from window:", data)

def edit_product():
    print("Edit product...")

def view_product():
    print("View product...")

def add_inventory():
    print("Add inventory...")

def edit_inventory():
    print("Edit inventory...")

def view_inventory():
    print("View inventory...")

def add_sale():
    print("Add sale...")

def edit_sale():
    print("Edit sale...")

def view_sale():
    print("View sale...")

def reports():
    print("View Reports")