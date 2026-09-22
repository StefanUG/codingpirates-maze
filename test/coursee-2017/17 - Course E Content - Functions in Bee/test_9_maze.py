from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions7")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/9



---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward() # limit: 6
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

def get_7_make_7():
    bee.right()
    bee.forward()
    for i in range(7):
        bee.get_nectar()
    bee.forward()
    for i in range(7):
        bee.make_honey()
    bee.backward()
    bee.backward()
    bee.left()

# Start
bee.forward()
get_7_make_7()
for i in range(3):
    bee.forward()
get_7_make_7()

# Keep this
Puzzle.done()