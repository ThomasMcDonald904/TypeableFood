from utils import ChopStateError


class Ingredient():
  def __init__(self):
    self.name = self.__name__
    self.chop_state = 0

  def chop(chop_state_wanted: int):
    if not chop_state_wanted < self.chop_state:
      self.chop_state = chop_state_wanted
    else:
      raise ChopStateError
      

class Apple(Ingredient):
  def __init__(self):
    pass