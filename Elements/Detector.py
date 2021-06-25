import numpy as np
from Elements import Muon as mu
import queue as q
from scipy import constants as cst


class Detector(object):
    '''A rudimentary class for a cylindrical detector'''

    def __init__(self, radius, height, name, position = np.array([0.,0.,0.])):
        '''Constructor for cylindrical detector
        Arguments:
            radius (meters)
            height (meters)
            position (meters) position of CENTER of detector
            '''

        self.radius = radius
        self.height = height
        self.position = position

        self.fill = "Water"
        self.slantDepth = 6.011 #km w.e.
        self.wallThickness = 2.54 #cm
        self.name = name

    def isInside(self, point):
        '''Returns a boolean indicating whether or not a point in 3-space
            is inside the detector. (Assumes Cartesian coords)

            Argument : point (array-type object of size 3)
        '''

        detX = self.position[0]
        detY = self.position[1]
        detZ = self.position[2]

        x = point[0]
        y = point[1]
        z = point[2]

        if x > detX + self.radius or x < detX - self.radius:
            return False
        elif y > detY + self.radius or y < detY - self.radius:
            return False
        elif z > detZ + self.height or z < detZ:
            return False
        else:
            return True

    def __str__(self):
        '''Renders relevant Detector details into a string'''
        string = self.name + " —>[Rad: " + str(self.radius) + "m , Ht: " + str(self.height) + "m , Thk: "\
         + str(self.wallThickness) + "cm ] Pos:" + str(self.position) +"\n"
        return string

    def testIntersection(self, muon):
        '''Returns entry and exit points of a muon passing through the detector.
            If the muon does not intersect, returns None
        '''

        #First check if the argument is a muon:
        if not isinstance(muon, mu.Muon):
            print("Non-Muon argument; returning None.")
            return None

        #Calculate how many checks are necessary: 1 every cm
        track = muon.mu.getTrack()
        maxX = abs(track[0]) + self.radius + abs(self.position[0]) #these position values will probably be zero
        maxY = abs(track[2]) + self.radius + abs(self.position[1])
        maxZ = abs(track[4])
        iterator = int(100*sqrt(maxX**2 + maxY**2 + maxZ**2))
        #something like the highest possible number of centimeters

        muPos = np.array([track[0], track[2], track[4]]) #see convention, x,y,z (muon.py)

        #instantiate test queue to determine entry/exit points
        intersectionQueue = q.queue(maxsize=2)

        for i in range(iterator):
            #check if the point is inside
            #if isInside(muPos):

            pass

            #calculate the point of the muon, move it ahead a bit (maintain direction)
