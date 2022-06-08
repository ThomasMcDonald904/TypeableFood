from core import printList
inventory = []
devInventory = []

def inventoryCheck(inventoryType, dev):
    if inventoryType == "fridge":
        if dev:
            printList(devInventory)
        else:
            printList(inventory)
    