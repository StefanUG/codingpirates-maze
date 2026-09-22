from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseE_farmer_concept2")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/19/levels/7



---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.left()
farmer.right()
farmer.pick_pumpkin()
for i in range(???):
    # Do this
while farmer.has_pumpkin():
    # Do this
while farmer.path_ahead():
    # Do this
if farmer.path_left():
    # Do this
if farmer.path_left():
    # Do this
else:
    # Otherwise this
def do_something():


do_something()
```
'''

# When run

def get_pumpkin():
    farmer.right()
    for i in range(2):
        farmer.forward()
        farmer.pick_pumpkin()
    for i in range(2):
        farmer.backward()
    farmer.left()

# Start
while farmer.path_ahead():
    farmer.forward()
    if farmer.path_right():
        get_pumpkin()

# Keep this
Puzzle.done()