from maze import Puzzle, Harvester

maze = Puzzle.from_file("courseF_bee_fwp_challenge1")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/24/levels/10

Use one `for loop` in a function to collect all of the corn. The same `for loop` can count to different maximum values by using the `length` parameter.

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

farmer.forward()
farmer.right()
farmer.left()
farmer.pick_corn() # limit: 1

#
# Loops

for i in range():
    # Do this
for counter in range(1, 2, 1):

counter

#
# Conditionals

if farmer.has_lettuce():
    # Do this
if farmer.has_corn():
    # Do this
else:
    # Otherwise this

#
# Functions



#
# Math

1
```
'''

# When run

def pick_row(length):
    farmer.left()
    for counter in range(1, length+1, 1):
        farmer.forward()
        for i in range(counter):
            farmer.pick_corn()
    for i in range(length):
        farmer.backward()
    farmer.right()

# Start
pick_row(length=3)
farmer.forward()
farmer.forward()
pick_row(length=5)
farmer.forward()
farmer.forward()
pick_row(length=6)
farmer.forward()
farmer.forward()
pick_row(length=4)

# Keep this
Puzzle.done()