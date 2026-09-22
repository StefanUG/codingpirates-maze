from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseE_bee_functions_challenge1")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/17/levels/14

You are on your own for this challenge.  This could "bee" harder than it looks!

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.right()
bee.left()
bee.get_nectar()
bee.make_honey()

#
# Loops

for i in range(???):
    # Do this

#
# Conditionals

if bee.at_flower():
    # Do this
else:
    # Otherwise this
if bee.at_flower():
    # Do this

#
# Functions


```
'''

# When run

def get_3_nectar_or_honey():
    for i in range(3):
        bee.forward()
        bee.forward()
        bee.left()
        bee.forward()
        if bee.at_flower():
            bee.get_nectar()
        else:
            bee.make_honey()
        bee.backward()
        bee.right()

# Start
get_3_nectar_or_honey()
for i in range(2):
    bee.forward()
    bee.right()
    bee.forward()
get_3_nectar_or_honey()

# Keep this
Puzzle.done()