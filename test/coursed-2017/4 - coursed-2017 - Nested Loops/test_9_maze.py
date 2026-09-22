from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_nestedLoops7")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/4/levels/9

**Challenge:** Figure out how to get all of the nectar using only the blocks available.

---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward() # limit: 2
bee.left()
bee.right()
bee.get_nectar() # limit: 1
bee.make_honey()
for i in range(???): # limit: 3
    # Do this
```
'''

# When run

# Start
for i in range(4):
    for i in range(3):
        for i in range(12):
            bee.get_nectar()
        bee.forward()
    bee.right()

# Keep this
Puzzle.done()