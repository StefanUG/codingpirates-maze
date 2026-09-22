from maze import Puzzle, Collector

maze = Puzzle.from_file("courseD_collector_debugging_challenge2")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursed-2017/lessons/8/levels/12



---
Here are elements from the toolbox.
You can use them in your code:
```
collector.forward()
collector.backward()
collector.left()
collector.right()
for i in range(3): # limit: 4
    # Do this
collector.collect() # limit: 1
```
'''

# When run

# Start
for i in range(4):
    for i in range(4):
        for i in range(2):
            collector.forward()
            for i in range(2):
                collector.collect()
        collector.backward()
    collector.right()

# Keep this
Puzzle.done()