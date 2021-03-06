import os


class InventoryTypeError(Exception):
    def __init__(self, message: str = "Wrong inventory type given."):
        self.msg = message
        super(InventoryTypeError, self).__init__(self.msg)

class ChopStateError(Exception):
  def __init__(self, message: str = "chop_state_given must be smaller than current chop state; You can't unchop"):
    self.msg = message
    super(ChopStateError, self).__init__(self.msg)

def os_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
    


def print_list(_list):
    for item in _list:
        print("    - ", item.capitalize())
