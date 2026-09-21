from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while3_2024")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/16/levels/3

*"Move to the pile of dirt and tell me how many shovelfuls to remove."*

Use as few blocks as possible to solve this puzzle.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.remove()
farmer.fill()
for i in range(5):
    # Do this
```
'''

# When run

# Start
farmer.forward()
for i in range(10):
    farmer.remove()

# Keep this
Puzzle.done()