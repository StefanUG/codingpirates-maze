import turtle
"""
Module to capture a turtle screen into image files
"""

def capture(screen:turtle.Screen, filename=None):
  # desktop-only tool: subprocess/datetime are unavailable under Skulpt, so import lazily
  import datetime
  import subprocess

  if (not filename):
    dt = datetime.datetime.now()
    filename = dt.strftime("%Y-%m-%d %H.%M.%S") + " screen"

  psfile = filename + ".ps"
  canvas = screen.getcanvas() 
  canvas.postscript(file=psfile)
  print("captured screen to ps file " + psfile)

  try:
    subprocess.run(f"convert '{psfile}' '{filename}.png'", shell=True)
    print(" - converted to PNG: " + filename + ".png")
  except:
    print("Failed to convert to PNG")
