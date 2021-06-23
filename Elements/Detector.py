import numpy as np
from scipy import constants as cst


class Detector(object):
    '''A rudimentary class for a cylindrical detector'''


    def __init__(self, radius, height, position = np.array([0.,0.,0.])):
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

    #def testIntersection(self, track):
        '''Returns a boolean indicating whether or not a muon's track intersects
            with the detector'''

            #Calculate how many checks are necessary: 1 every cm
'''
        maxX = abs(track[0]) + self.radius + abs(self.position[0]) #these position values will probably be zero
        maxY = abs(track[1]) + self.radius + abs(self.position[1])
        maxZ = abs(track[2])

        iterator = int(100*sqrt(maxX**2 + maxY**2 + maxZ**2))

        muX = track[0]
        muY = track[1]
        muZ = track[2]

        for i in range(iterator):
            #calculate the point of the muon, move it ahead a bit (maintain direction)
'''

    
