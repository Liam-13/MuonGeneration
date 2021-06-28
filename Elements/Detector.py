import numpy as np
from Elements import Muon as mu
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
            [x1,y1,z1,x2,y2,z2]
            If the muon does not intersect, returns None
        '''

        #First check if the argument is a muon:
        if not isinstance(muon, mu.Muon):
            print("Non-Muon argument; returning None.")
            return None

        #Calculate how many checks are necessary: 1 every cm
        track = muon.getTrack()
        maxX = abs(track[0]) + self.radius + abs(self.position[0]) #these position values will probably be zero
        maxY = abs(track[2]) + self.radius + abs(self.position[1])
        maxZ = abs(track[4])
        iterator = int(100*np.sqrt(maxX**2 + maxY**2 + maxZ**2))
        #something like the highest possible number of centimeters

        muPos = np.array([track[0], track[2], track[4]]) #see convention, x,y,z (muon.py)
        muDir = np.array([track[1], track[3], track[5]])

        #instantiate tuple for entry/exit testing
        intersectionQueue = [False, False]
        entry = np.empty(3)
        exit = np.empty(3)

        for i in range(iterator):

            if intersectionQueue == [False, True]:
                #we found the entry point
                entry = muPos
            elif intersectionQueue == [True, False]:
                #we found the exit point
                exit = muPos
                return np.append(entry,exit)
            elif i == iterator:
                return None


            #Move point over
            intersectionQueue[0] = intersectionQueue[1]
            #check if the point is inside
            if self.isInside(muPos):
                intersectionQueue[1] = True
            else:
                intersectionQueue[1] = False
                if i > iterator/2:
                    return None

            #calculate the point of the muon, move it ahead a bit (maintain direction)
            muPos += muDir*2 # 2cm at a time?
