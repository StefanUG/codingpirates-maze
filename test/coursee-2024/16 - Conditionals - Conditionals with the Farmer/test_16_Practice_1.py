from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_while1_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2024/lessons/16/levels/16

Move forward until you get to the lettuce, then turn left **if** there is a path to the left.  Otherwise, turn right.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward() # limit: 1
farmer.right()
farmer.left()
farmer.pick_lettuce()
if farmer.path_left():
    # Do this
else:
    # Otherwise this
while farmer.has_lettuce():
    # Do this
while not farmer.has_lettuce():
    # Do this
for i in range(5):
    # Do this
# 
```
'''

# When run

# Start
for i in range(9):
    while not farmer.has_lettuce():
        farmer.forward()
    while farmer.has_lettuce():
        farmer.pick_lettuce()
    if farmer.path_left():
        farmer.left()
    else:
        farmer.right()

# Keep this
Puzzle.done()