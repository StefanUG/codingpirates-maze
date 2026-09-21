from maze import Puzzle, Collector

maze = Puzzle.from_file("courseB_collector_loops_challenge1_2024")
collector: Collector = maze.player

'''
https://studio.code.org/s/courseb-2024/lessons/8/levels/14

This time you have limited blocks. Get all of the treasure! 

---
Here are elements from the toolbox.
You can use them in your code:
```
collector.east()
collector.west()
collector.north()
collector.south()
collector.collect()
for i in range(???):
    # Do this
```
'''

# When run

# Start
for i in range(5):
    collector.south()
    collector.collect()
collector.east()
collector.east()
for i in range(5):
    collector.collect()
    collector.north()
collector.east()
collector.east()
for i in range(5):
    collector.south()
    collector.collect()

# Keep this
Puzzle.done()