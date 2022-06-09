from utils import print_list, InventoryTypeError

fridge = []
devFridge = ["Apple", "Cheese", "Chocolate"]

pantry = []
devPantry = ["Rice", "Flour", "Sugar"]

def inventory_item_check(inventory, item, dev):
    if dev:
        if inventory == "fridge" and item in devFridge:
            return True
        elif inventory == "pantry" and item in devPantry:
            return True
        else:
            return False
    else:
        if inventory == "fridge" and item in fridge:
            return True
        elif inventory == "pantry" and item in pantry:
            return True
        else:
            return False

def inventory_check(inventory_type, dev):
    if inventory_type == "fridge":
        print("Fridge Inventory: ")
        if dev:
            print_list(devFridge)
        else:
            print_list(fridge)

    elif inventory_type == "pantry":
        print("Pantry Inventory: ")
        if dev:
            print_list(devPantry)
        else:
            print_list(pantry)

    else:
        raise InventoryTypeError


