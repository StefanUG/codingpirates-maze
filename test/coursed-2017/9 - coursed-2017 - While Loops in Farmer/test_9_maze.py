from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while7")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/9/levels/9



---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward() # limit: 1
farmer.right()
farmer.left()
farmer.remove()
farmer.fill()
for i in range(5): # limit: 1
    # Do this
while farmer.path_ahead():
    # Do this
```
'''

# When run

# Start
for i in range(4):
    while farmer.path_ahead():
        farmer.forward()
    farmer.fill()
    farmer.left()

# Keep this
Puzzle.done()