from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_nestedLoops6")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/4/levels/8

*"Must eat sunflower!"*

Get the zombie to the sunflower using only the blocks available.

---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward() # limit: 2
zombie.left()
zombie.right()
for i in range(???): # limit: 4
    # Do this
```
'''

# When run

# Start
for i in range(3):
    for i in range(5):
        zombie.forward()
    zombie.left()
for i in range(2):
    for i in range(3):
        zombie.forward()
    zombie.left()

# Keep this
Puzzle.done()