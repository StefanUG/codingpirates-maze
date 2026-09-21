from maze import Puzzle, Harvester

maze = Puzzle.from_file("CourseD_2022_LessonExtra14b_2024")
farmer: Harvester = maze.player

'''
https://studio.code.org/s/coursed-2024/lessons/15/levels/17

*"I need some help on the farm! Help me harvest this corn using only the blocks in your toolbox."*

---
Here are elements from the toolbox.
You can use them in your code:
```
farmer.forward()
farmer.right()
farmer.left()
farmer.pick_corn()
for i in range(5):
    # Do this
```
'''

# When run

# Start
for i in range(3):
    for i in range(2):
        farmer.forward()
        farmer.left()
        farmer.forward()
        farmer.right()
    for i in range(5):
        farmer.pick_corn()

# Keep this
Puzzle.done()