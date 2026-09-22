from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_nested_loops_challenge2a")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/4/levels/14

*"Let's hunt for treasure - using loops!"* 

Help Laurel collect at least two piles of treasure using only the blocks in your toolbox. It is possible to collect all 4.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward() # limit: 3
collector.right()
collector.left()
for i in range(???):
    # Do this
collector.collect() # limit: 2
```
'''

# When run

# Start
for i in range(2):
    collector.collect()
    for i in range(3):
        collector.forward()
    collector.right()
    for i in range(3):
        collector.forward()

# Keep this
Puzzle.done()