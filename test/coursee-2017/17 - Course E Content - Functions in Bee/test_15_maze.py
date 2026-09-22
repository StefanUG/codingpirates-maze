from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions_challenge2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/15



---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward() # limit: 5
bee.right()
bee.left()
bee.get_nectar() # limit: 1
bee.make_honey() # limit: 1

#
# Loops

for i in range(???):
    # Do this

#
# Functions


```
'''

# When run

def move_and_collect():
    bee.left()
    bee.forward()
    bee.forward()
    for i in range(6):
        bee.get_nectar()
    for i in range(2):
        bee.forward()
        for i in range(3):
            bee.make_honey()
    bee.forward()

# Start
for i in range(3):
    move_and_collect()
bee.right()
bee.forward()
bee.right()
bee.right()
move_and_collect()

# Keep this
Puzzle.done()