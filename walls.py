# IMPORTS ---------------------------------------------------------------------------------------- #

import random

# GLOBALS ---------------------------------------------------------------------------------------- #

world_width = 32
world_height = 32

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
    world[row_num].insert(col_num, '   ')

# PLACE NORTH OUTSIDE ---------------- #

nw_corner_row = random.randint(0,1)
nw_corner_col = random.randint(0,1)
world[nw_corner_row][nw_corner_col] = ' # '

north_num_sections = random.randint(2,5)
ne_corner_row = nw_corner_row ^ (1 if (north_num_sections % 2 == 0) else 0)
ne_corner_col = world_width - random.randint(1,2)
world[ne_corner_row][ne_corner_col] = ' # '

sections = [ ne_corner_col - nw_corner_col - 1 ]
for i in sections: print(i,end=' ')
print()

while len(sections) < north_num_sections:
  i = random.randint(0, len(sections)-1) # TODO: Bias proportionately towards larger sections
  if (sections[i] <= 2):
    print('FAIL')
    continue
  left = random.randint(1, sections[i]-2) # TODO: Bias if current section is large
  right = sections[i] - left - 1
  print(f'L:{left} R:{right}')
  sections[i] = right
  sections.insert(i, left)

  for i in sections: print(i,end=' ')
  print()

c = nw_corner_col
for i in range(len(sections)):
  for j in range(c,c+sections[i]+2):
    world[nw_corner_row^(i&1)][j] = ' # '
  c += sections[i] + 1

# TODO: West, South, and East outside walls



print_world()
