from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseC_harvester_loops9_2025")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursec-2025/lessons/9/levels/10

Collect all of the corn and all of the pumpkins.

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.pick_pumpkin()
farmer.pick_corn()
for i in range(5):
    # Do this
```
'''

# When run

# Start
for i in range(5):
    farmer.forward()
    farmer.pick_corn()
farmer.left()
farmer.forward()
farmer.left()
for i in range(6):
    farmer.pick_pumpkin()
    farmer.forward()

# Keep this
Puzzle.done()