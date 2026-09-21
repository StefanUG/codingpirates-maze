from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_conditionals5_2025")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/16/levels/6



---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.right()
bee.left()
bee.get_nectar()
bee.make_honey()
if bee.at_flower():
    # Do this
for i in range(???):
    # Do this
```
'''

# When run

# Start
for i in range(2):
    for i in range(6):
        bee.forward()
        if bee.at_flower():
            bee.get_nectar()
    bee.left()
    bee.forward()
    bee.forward()
    bee.left()

# Keep this
Puzzle.done()