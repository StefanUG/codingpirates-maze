from maze import Puzzle, Bird

maze = Puzzle.from_file("courseC_maze_programming8_predict1_2025")
bird: Bird = maze.player

'''
https://studio.code.org/s/coursec-2025/lessons/3/levels/10

*"Keep calm and help me find the bad pig."*

---
Here are elements from the toolbox.
You can use them in your code:
```
bird.forward()
bird.left()
bird.right()
for i in range(???):
    # Do this
```
'''

# When run

# Start
bird.forward()
bird.right()
bird.forward()
bird.forward()
bird.forward()
bird.forward()
bird.right()
bird.forward()

# Keep this
Puzzle.done()