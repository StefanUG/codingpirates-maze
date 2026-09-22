from maze import Puzzle, Collector

maze = Puzzle.from_file("courseC_collector_prog9_2025")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2025/lessons/5/levels/10

*"Let's get all of the treasure!"*

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.right()
collector.left()
for i in range(???):
    # Do this
collector.collect()
```
'''

# When run

# Start
collector.forward()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.forward()
collector.collect()

# Keep this
Puzzle.done()