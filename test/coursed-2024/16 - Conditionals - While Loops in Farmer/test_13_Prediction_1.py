from maze import Puzzle, Farmer

maze = Puzzle.from_file("courseD_farmer_while10_predict2_2024")
farmer: Farmer = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/16/levels/13



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
while farmer.path_ahead():
    # Do this
```
'''

# When run

# Start
for i in range(3):
    while farmer.path_ahead():
        farmer.forward()
    while farmer.at_pile():
        farmer.remove()
    farmer.left()
    while farmer.path_ahead():
        farmer.forward()
    farmer.right()

# Keep this
Puzzle.done()