from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_nestedLoops5_2024")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/12/levels/8



---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward()
zombie.left()
zombie.right()
for i in range(???): # limit: 3
    # Do this
# 
```
'''

# When run

# Start
for i in range(2):
    for i in range(3):
        zombie.forward()
    zombie.left()
    for i in range(3):
        zombie.forward()
    zombie.right()

# Keep this
Puzzle.done()