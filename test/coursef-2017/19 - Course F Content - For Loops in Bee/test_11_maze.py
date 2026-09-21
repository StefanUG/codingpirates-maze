from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_for10")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/19/levels/11

**Challenge:** Take what you've learned about `for` loops and try to solve this problem. 

Remember: You may have to run through solutions multiple times before you figure out all of the steps.

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.get_nectar()
bee.right()
bee.left()

#
# Math

???
???*???

#
# Loops

for counter in range(1, 11, 1):

for i in range():
    # Do this

#
# Variables

counter
```
'''

# When run

# Start
for counter in range(14, -2, -4):
    bee.right()
    for i in range(int(counter/2)):
        bee.forward()
    for i in range(counter):
        bee.get_nectar()

# Keep this
Puzzle.done()