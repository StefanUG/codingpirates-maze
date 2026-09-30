import turtle
"""
Module to capture a turtle screen into image files
"""

def capture(screen:turtle.Screen, filename=None):
  # desktop-only tool: subprocess/datetime are unavailable under Skulpt, so import lazily
  import datetime
  import os
  import subprocess
  import sys

  if (not filename):
    dt = datetime.datetime.now()
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    #filename = os.path.join(script_dir, dt.strftime("%Y-%m-%d %H.%M.%S") + " screen")
    filename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    filename = os.path.join(script_dir, filename)

  psfile = filename + ".ps"
  canvas = screen.getcanvas() 
  canvas.postscript(file=psfile)
  print("captured screen to ps file " + psfile)

  try:
    subprocess.run(f"convert '{psfile}' '{filename}.png'", shell=True)
    print(" - converted to PNG: " + filename + ".png")
  except:
    print("Failed to convert to PNG")
