from inventorychecks import inventory_check, inventory_item_check
from utils import print_list

import os

isDev = True

available_inventories = ["Fridge", "Pantry"]


def handle_inventory_input():
    player_input = get_player_input("What inventory to check")
    if player_input == "fridge" or player_input == "f":
        inventory_check("fridge", isDev)
    elif player_input == "pantry" or player_input == "p":
        inventory_check("pantry", isDev)
    elif player_input == "help":
        print("You can type \"i\" then these to obtain your current available inventories")
        print_list(available_inventories)
    else:
        print("Inventory not available")


def get_player_input(input_info_message: str = ""):
    if not input_info_message == "":
        print(input_info_message)
    player_input = input("Input: ")
    os.system("cls")
    return player_input.lower()


def player_help(player_input):
    if "inventory" in player_input:
        print("You can type these to obtain your current available inventories")
        print_list(available_inventories)
    else:
        print("You can enter the inventory prompt by typing \"i\" then specifying which inventory you want.")
        print("More help can be obtained by typing \"help\" in the inventory prompt or by typing \"help inventory\" outside of the inventory prompt")


def handle_prepare_input():
    player_input = get_player_input("From which inventory will you get your ingredients from")
    if player_input == "fridge" or player_input == "f" and "fridge" in available_inventories:
        player_input = get_player_input("Which ingredient do you want from the fridge")
        if inventory_item_check("fridge", player_input, isDev):
            player_input = get_player_input("How do you want your ingredient prepared")
            # TODO add different preparation methods for both fridge and pantry
    elif player_input == "pantry" or player_input == "p" and "pantry" in available_inventories:
        player_input = get_player_input("Which ingredient do you want from the pantry")
        if inventory_item_check("pantry", player_input, isDev):
            player_input = get_player_input("How do you want your ingredient prepared")
    else:
        print("Inventory not available")



def game_loop():
    player_input = get_player_input()

    if player_input == "inventory" or player_input == "i":
        handle_inventory_input()
        game_loop()

    if player_input == "prepare" or player_input == "prep" or player_input == "p":
        handle_prepare_input()
        game_loop()
    # TODO add cooking
    if "help" in player_input:
        player_help(player_input)
        game_loop()
    else:
        print("Incorrect input")


print("Welcome to TypeableFood")
while True:
    game_loop()
