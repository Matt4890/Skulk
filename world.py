# OBJECTS ---------------------------------------------------------------------------------------- #

# TILE --------------------------------------------------- #

class Tile:
  def __init__(self, char, name):
    self.char = char
    self.name = name
  
  def __repr__(self):
    return self.name + " tile"

TILE_FLOOR = Tile(".", "Floor")
TILE_WALL = Tile("#", "Wall")
TILE_DOOR = Tile("^", "Door")

# ITEM --------------------------------------------------- #

class Item:
  def __init__(self, char, name, value):
    self.char = char
    self.name = name
    self.value = value
  
  def __repr__(self):
    return self.name + " item worth $" + str(self.value)

ITEM_GOLD = Item("G", "Gold", 1)
ITEM_SWORD = Item("S", "Sword", 10)
ITEM_WASHING_MACHINE = Item("W", "Washing Machine", 50)

# ROOM --------------------------------------------------- #

class Room:
  def __init__(self, w, h):
    # Set basic attributes
    self.width = w
    self.height = h

    # Generate tiles
    self.tiles = []
    for row_num in range(self.height):
      self.tiles.insert(row_num, [])
      for col_num in range(self.width):
        if col_num == 0 or col_num == (self.width - 1) or row_num == 0 or row_num == (self.height - 1):
          self.tiles[row_num].insert(col_num, TILE_WALL)
        else:
          self.tiles[row_num].insert(col_num, TILE_FLOOR)

    # Generate tiles
    # TODO
  
  def __repr__(self):
    s = "Room with width " + str(self.width) + " and height " + str(self.height) + "\n"
    for row_num in range(self.height):
      for col_num in range(self.width):
        s += self.tiles[row_num][col_num].char + " "
      s += "\n"

    return s