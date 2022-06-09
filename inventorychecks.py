from utils import print_list, InventoryTypeError
import ingredients

fridge = []
devFridge = [Apple(), "cheese", "chocolate"]
# TODO start work importing ingredients and creating classes

pantry = []
devPantry = ["rice", "flour", "sugar"]

def inventory_item_check(inventory, item, dev):
    if dev:
        if inventory == "fridge" and item.lower() in devFridge:
            return True
        elif inventory == "pantry" and item.lower() in devPantry:
            return True
        else:
            return False
    else:
        if inventory == "fridge" and item.lower() in fridge:
            return True
        elif inventory == "pantry" and item.lower() in pantry:
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


