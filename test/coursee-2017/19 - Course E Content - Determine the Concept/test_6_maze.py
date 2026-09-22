from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_concept4")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/19/levels/6



---
Here are elements from the toolbox.
You can use them in your code:
```
bee.forward()
bee.left()
bee.right()
bee.get_nectar()
bee.make_honey()
for i in range(???):
    # Do this
while bee.nectar() == 0:
    # Do this
while bee.path_ahead():
    # Do this
bee_ifNectarAmount
if bee.at_flower():
    # Do this
if bee.at_flower():
    # Do this
else:
    # Otherwise this
if bee.path_ahead():
    # Do this
else:
    # Otherwise this
if bee.path_ahead():
    # Do this
def honey_nectar():


honey_nectar()
```
'''

# When run

# Start
while bee.path_ahead():
    bee.forward()
    while bee.nectar() > 0:
        bee.get_nectar()
    while bee.honey() > 0:
        bee.make_honey()
    bee.right()
    bee.forward()
    bee.left()

# Keep this
Puzzle.done()