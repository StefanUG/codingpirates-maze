from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions13_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2024/lessons/17/levels/12

Solve this puzzle in 23 blocks or less.
___  

##### Each sprout will either grow *one* corn or nothing. To find the best solution, you will need to edit the functions directly.

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
farmer.pick_lettuce()

#
# Loops

for i in range(???):
    # Do this
while not farmer.at_pumpkin():
    # Do this
while farmer.has_corn():
    # Do this
while farmer.has_lettuce():
    # Do this
while farmer.path_ahead():
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
if farmer.has_lettuce():
    # Do this
if farmer.has_corn():
    # Do this
while not farmer.has_lettuce():
    # Do this
while farmer.has_corn():
    # Do this
while farmer.has_lettuce():
    # Do this
while farmer.path_ahead():
    # Do this

#
# Functions



#
# Comments

# 
```
'''

# When run

def lettuce_stairs():
    for i in range(2):
        farmer.forward()
        farmer.right()
        farmer.forward()
        farmer.left()
        while farmer.has_lettuce():
            farmer.pick_lettuce()

def corn_rectangle():
    for i in range(4):
        while farmer.path_ahead():
            farmer.forward()
            if farmer.has_corn():
                farmer.pick_corn()
        farmer.left()

# Start
lettuce_stairs()
corn_rectangle()
lettuce_stairs()

# Keep this
Puzzle.done()