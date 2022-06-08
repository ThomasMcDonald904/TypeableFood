from inventorycheck import inventory_check


def gameLoop():
    playerInput = input("Input: ")
    if playerInput.lower == "fridge" or "f":
        inventory_check("fridge", False)
    else:
        print("Incorrect Input")


print("Welcome to TypeableFood")
while True:
    gameLoop()
