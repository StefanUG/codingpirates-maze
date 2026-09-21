from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_nestedLoops9_2025")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/13/levels/12

Make all of the honey.

![]()

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left()
bee.right()
bee.get_nectar()
bee.make_honey()
for i in range(???):
    # Do this
# 
```
'''

# When run

# Start
for i in range(2):
    for i in range(5):
        bee.forward()
        bee.make_honey()
    bee.left()

# Keep this
Puzzle.done()