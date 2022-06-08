from utils import print_list

inventory = []
devInventory = ["Apple", "Cheese", "Chocolate"]


def inventory_check(inventoryType, dev):
    if inventoryType == "fridge":
        if dev:
            print_list(devInventory)
        else:
            print_list(inventory)
