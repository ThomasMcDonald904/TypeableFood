
class InventoryTypeError(Exception):
    def __init__(self, message: str = 'Wrong inventory type given.'):
        self.msg = message
        super(InventoryTypeError, self).__init__(self.msg)


def print_list(_list):
    for item in _list:
        print("    - ", item)
