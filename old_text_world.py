
# IMPORTS ---------------------------------------------------------------------------------------- #

import random

# GLOBALS ---------------------------------------------------------------------------------------- #

world_width = 10
world_height = 10

"""
[
  [T00, T01, T02, ... , T09],
  [T10, T11, T12, ... , T19],
  [T20, T21, T22, ... , T29],
  [ ... ],
  [T90, T91, T92, ... , T99]
]

world[0][0] -> T00
world[1][2] -> T12
"""
world = []

# FUNCTIONS -------------------------------------------------------------------------------------- #

def print_world():
  for row_num in range(world_height):
    for col_num in range(world_width):
      print(world[row_num][col_num], end='')
    print()
  print()

# MAIN ------------------------------------------------------------------------------------------- #

# GENERATE BLANK WORLD --------------- #

for row_num in range(world_height):
  # print("Generating row", row_num)
  world.insert(row_num, [])
  for col_num in range(world_width):
    # print("Generating row", row_num, "column", col_num)
    world[row_num].insert(col_num, ".")

print_world()

# PLACE WALLS ------------------------ #

for row_num in range(world_height):
  for col_num in range(world_width):
    if col_num == 0 or col_num == 9 or row_num == 0 or row_num == 9:
      world[row_num][col_num] = "#"

print_world()

# PLACE ITEMS ------------------------ #

potential_items = ["G", "S", "W"]

for row_num in range(1, world_height - 1):
  for col_num in range(1, world_width - 1):
    is_item_present = (random.randint(0,9) == 0)  # 10% chance
    if is_item_present:
      world[row_num][col_num] = random.choice(potential_items)

print_world()

# PLACE ENTITIES --------------------- #

for row_num in range(1, world_height - 1):
  for col_num in range(1, world_width - 1):
    is_enemy_present = (random.randint(0,19) == 0)  # 5% chance
    if is_enemy_present:
      world[row_num][col_num] = "E"

print_world()

world[2][2] = "@"

print_world()
