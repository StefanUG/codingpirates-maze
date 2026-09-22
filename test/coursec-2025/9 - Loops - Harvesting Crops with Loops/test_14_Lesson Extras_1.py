from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseC_harvester_loops_challenge1a_2025")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursec-2025/lessons/9/levels/14



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
for i in range(2):
    farmer.forward()
    farmer.pick_corn()
farmer.right()
for i in range(2):
    for i in range(4):
        farmer.forward()
        farmer.pick_corn()
    farmer.right()
for i in range(6):
    farmer.forward()
    farmer.pick_corn()

# Keep this
Puzzle.done()