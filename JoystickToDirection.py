
import math
from typing import List


deadspace = 0.1
maxval = 1

#This places the coords on a value from 100 to -100
def standardizedCoOrds(x, y):
    x = x/30000
    y = y/30000
    return(x,y)

#converts coordinates into a value returning magnitude and angle
def coordinatesToVector(xval,yval):
    tuple = standardizedCoOrds(xval,yval)
    (x, y) = tuple
    magnitudeOfVector = math.sqrt(x**2 + y**2)
    if magnitudeOfVector <= deadspace:
        magnitudeOfVector = 0
    if magnitudeOfVector >= maxval:
        magnitudeOfVector = 1
    directionOfVector = abs(math.degrees(math.atan(y/x)))
    return (magnitudeOfVector, directionOfVector)

#converts coordinates into a 3 figure bearing with magnitude
def coordinatesToBearing(joyX, joyY):
    tuple = coordinatesToVector(joyX, joyY)
    magnitude = tuple[0]
    angle = abs(tuple[1])
    if joyX >= 0 and joyY >= 0:
        bearing = 90 - angle
    elif joyX >= 0 and joyY <= 0:
        bearing = 180 - angle
    elif joyX <= 0 and joyY <= 0:
        bearing = 270 - angle
    elif joyX >= 0 and joyY <= 0:
        bearing = 360 - angle
    return(magnitude * 100, int(bearing))
