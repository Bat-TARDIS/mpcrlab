#!usr/bin/python
# Import Color Tracking
import track_color
import Rover20

class RoverMovingToColor:

  def RoverMain ():
      rover = Rover20()
      move_rover = track_color.bestContour
      if move_rover == True:
          rover.setTreads(1,1)

  RoverMain()