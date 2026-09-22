from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops6_2025")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2025/lessons/8/levels/8

Figure out the code to help Laurel get all of the treasure!

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east() # limit: 1
collector.west() # limit: 1
collector.north()
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
    collector.south()
    collector.collect()
for i in range(5):
    collector.west()
    collector.collect()

# Keep this
Puzzle.done()