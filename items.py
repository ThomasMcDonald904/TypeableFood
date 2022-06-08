def Ingredient():
    def __init__(self, type: str, name: str):
        self.type = type
        self.name = name

class Flour(Ingredient):
    