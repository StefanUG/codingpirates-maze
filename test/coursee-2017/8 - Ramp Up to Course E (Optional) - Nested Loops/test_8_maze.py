from maze import Puzzle, ZombiePlayer

maze = Puzzle.from_file("courseD_maze_nestedLoops5")
zombie: ZombiePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/8/levels/8



---
Here are elements from the toolbox.
You can use them in your code:
```
zombie.forward()
zombie.left()
zombie.right()
for i in range(???): # limit: 3
    # Do this
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