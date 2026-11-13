import csv

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
        return "error"