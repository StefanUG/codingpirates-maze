from maze import Puzzle, Collector

maze = Puzzle.from_file("grade2_collector_10_2025")
collector: Collector = maze.player

'''
https://studio.code.org/s/coursec-2025/lessons/5/levels/13

You're almost done!  

Collect as many pieces of treasure as you can to finish the stage!

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
collector.collect()
collector.forward()
collector.collect()
collector.forward()
collector.collect()
collector.left()
collector.forward()
collector.left()
collector.collect()
collector.forward()
collector.collect()
collector.forward()
collector.collect()
collector.right()
collector.forward()
collector.right()
collector.collect()
collector.forward()
collector.collect()
collector.forward()
collector.collect()

# Keep this
Puzzle.done()