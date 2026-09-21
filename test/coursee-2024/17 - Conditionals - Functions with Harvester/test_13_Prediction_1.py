from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions11_predict_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2024/lessons/17/levels/13

Figure out which function to use and which one to delete, then solve this puzzle!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

farmer.forward()
farmer.right()
farmer.left()
farmer.pick_corn()
farmer.pick_pumpkin()
farmer.pick_lettuce()

#
# Loops

while farmer.has_corn():
    # Do this
while farmer.path_ahead():
    # Do this
while not farmer.has_pumpkin():
    # Do this
for i in range(5):
    # Do this

#
# Conditionals

if farmer.path_ahead():
    # Do this
if farmer.path_ahead():
    # Do this
else:
    # Otherwise this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this
if farmer.has_corn():
    # Do this

#
# Functions


```
'''

# When run

def get_all_pumpkins():
    while farmer.has_pumpkin():
        farmer.pick_pumpkin()

def get_produce():
    while not farmer.has_lettuce():
        farmer.forward()
    farmer.pick_lettuce()

def check_square_for_corn():
    if farmer.has_corn():
        farmer.pick_corn()

def pumpkin_square():
    for i in range(4):
        pick_along_path()
        farmer.right()

def pick_along_path():
    while not farmer.has_pumpkin():
        check_square_for_corn()
        farmer.forward()
    get_all_pumpkins()

# Start
while farmer.path_ahead():
    check_square_for_corn()
    farmer.forward()
farmer.right()
farmer.right()
get_produce()

# Keep this
Puzzle.done()