from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_until9_2025")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2025/lessons/18/levels/9

**Challenge:** Avoid the chompers and help the zombie get to the sunflower.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward() # limit: 2
zombie.right()
zombie.left()
while zombie.path_ahead():
    # Do this
while not zombie.at_finish():
    # Do this
if zombie.path_left():
    # Do this
# 
```
'''

# When run

# Start
zombie.right()
zombie.right()
zombie.forward()
zombie.right()
while not zombie.at_finish():
    while zombie.path_ahead():
        zombie.forward()
    zombie.left()

# Keep this
Puzzle.done()