from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_for_challenge2")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/19/levels/14

Solve this puzzle with the fewest number of blocks possible.

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.get_nectar()
bee.make_honey()

#
# Loops

for i in range():
    # Do this
for counter in range(1, 11, 1):

counter

#
# Math

???
???*???
```
'''

# When run

# Start
for counter in range(1, 4, 1):
    for i in range(counter):
        bee.forward()
    for i in range(counter):
        bee.get_nectar()
    bee.left()
    for i in range(counter):
        bee.forward()
    bee.right()
bee.right()
bee.right()
for counter in range(2, 12, 2):
    bee.forward()
    bee.left()
    bee.forward()
    bee.right()
    for i in range(counter):
        bee.make_honey()

# Keep this
Puzzle.done()