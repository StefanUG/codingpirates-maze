from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_fwp7")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/7

**Challenge:** Something looks a little different. Modify your function to make honey as well.

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

for i in range(1):

1
for counter in range(1, 11, 1):

counter

#
# Conditionals

if bee.at_flower():
    # Do this

#
# Functions

1
rowOfNectarOrHoney()

#
# Math

1
1+1
```
'''

# When run

def rowOfNectarOrHoney(width):
    for i in range(width):
        bee.forward()
        if bee.at_flower():
            bee.get_nectar()
        if bee.at_honeycomb():
            bee.make_honey()

# Start
for counter in range(1, 7, 1):
    bee.left()
    rowOfNectarOrHoney(width=counter)

# Keep this
Puzzle.done()