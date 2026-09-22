from maze import Puzzle, BeePlayer

maze = Puzzle.from_file("courseD_bee_nestedLoops8")
bee: BeePlayer = maze.player

'''
https://studio.code.org/s/coursee-2017/lessons/8/levels/11

Collect all of the nectar from each flower and make honey at the honeycomb. 

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
```
'''

# When run

# Start
for i in range(5):
    bee.forward()
    for i in range(4):
        bee.get_nectar()
bee.forward()
for i in range(4):
    bee.make_honey()

# Keep this
Puzzle.done()