from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseF_bee_for_challenge1")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursef-2017/lessons/19/levels/13

You can use this `for loop` to collect all of the nectar. Un-bee-lievable!

There are a few actions that you will want to `repeat 'counter' times`.

---
Here are elements from the toolbox.
You can use them in your code:
```

#
# Actions

bee.forward()
bee.backward()
bee.right()
bee.left()
bee.get_nectar() # limit: 1

#
# Loops

for i in range(counter):

counter

#
# Functions



#
# Math

1
```
'''

# When run

def move_and_get_nectar_with_counter():
    bee.right()
    for i in range(counter):
        bee.forward()
    for i in range(counter):
        bee.get_nectar()
    for i in range(counter):
        bee.backward()
    bee.left()

# Start
for counter in range(1, 9, 2):
    move_and_get_nectar_with_counter()
    bee.forward()
    bee.forward()

# Keep this
Puzzle.done()