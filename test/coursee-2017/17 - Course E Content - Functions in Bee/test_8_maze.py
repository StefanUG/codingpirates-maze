from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions6")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/8



---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
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

def get_7_nectar_make_7_honey():
    bee.forward()
    for i in range(7):
        bee.get_nectar()
    bee.forward()
    for i in range(7):
        bee.make_honey()

# Start
get_7_nectar_make_7_honey()
bee.forward()
get_7_nectar_make_7_honey()

# Keep this
Puzzle.done()