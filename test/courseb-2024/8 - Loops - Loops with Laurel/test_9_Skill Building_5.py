from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops7_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/8/levels/9

Write the code to get all of this treasure.

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east() # limit: 1
collector.west() # limit: 1
collector.north() # limit: 1
collector.south() # limit: 1
collector.collect()
for i in range(3):
    # Do this
```
'''

# When run

# Start
for i in range(4):
    collector.east()
    collector.collect()
for i in range(3):
    collector.north()
    collector.collect()
for i in range(3):
    collector.west()
    collector.collect()
collector.south()
collector.collect()

# Keep this
Puzzle.done()