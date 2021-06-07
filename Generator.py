####################################################
#                 Generator Class                  #
#      Disk-Shaped Generator for Particles         #
#        Based in Cylindrical Coordinates          #
####################################################
import random
import numpy as np
import math

class Generator:
    '''A Generator Class meant to yield positions for particles'''

    radius = 1.
    #Cylindrical coordinates
    centre = np.array([0.,0.,1.])

    def __init__(self, radius = 1., position = np.array([0.,0.,1.])):
        '''Generator constructor takes a radius and a position'''

        self.radius = radius
        self.centre = position

    def generatePositions(self, number):
        '''Generates a numpy array of absolute positions in cylindrical coordinates'''

        #Array for positions
                            #"number" of rows, each with 3 columns
        positions = np.empty((number,3))

        x_centre = self.centre[0]*np.cos(self.centre[1])
        y_centre = self.centre[0]*np.sin(self.centre[1])


        for i in range(number):
            theta = random.random()*np.pi*2
            rho = random.random()*self.radius #relative centre of generator disk

            x_rho = rho*np.cos(theta)
            y_rho = rho*np.sin(theta)

            realRho = math.sqrt((x_rho+x_centre)**2 + (y_rho+y_centre)**2) #With respect to absolute position, not just generator centre
            realTheta = np.arctan((y_rho+y_centre)/(x_rho+x_centre))

            positions[i] = [realRho, realTheta, self.centre[2]] #absolute positions

        return positions
