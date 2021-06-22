import numpy as np
import scipy as sp
from sp import constants as cst


class Detector(object):
    '''A rudimentary class for a cylindrical detector'''


    def __init__(self, radius, height, position = np.array([0.,0.,0.])):
        '''Constructor for cylindrical detector
        Arguments:
            radius (meters)
            height (meters)
            position (meters) position of bottom of detector
            '''

        self.radius = radius
        self.height = height
        self.position = position

        self.fill = "Water"
        self.slantDepth = 6.011 #km w.e.


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
