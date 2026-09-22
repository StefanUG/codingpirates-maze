from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_functions11_predict")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/18/levels/14

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



# Keep this
Puzzle.done()