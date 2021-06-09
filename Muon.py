####################################################
#                    Muon Class                    #
#        Muon Class for Storing Attributes         #
#               And Distribution Data              #
####################################################

import numpy as np
import random
import matplotlib.pyplot as plt

class Muon:
    '''A Muon class for sourcing the attributes and distribution functions for Muons'''

    #Muons have a position and momentum in Cylindrical Coordinates
    position = np.array(3)
    momentum = np.array(3)

    slantDepth = 6.011 #km w.e.
    I1 = 8.60e-6 # ± 0.53e-6 /sec/cm^2/sr
    I2 = 0.44e-6 # ± 0.06e-6 /sec/cm^2/sr
    lam1 = 0.45 # ± 0.01 km.w.e.
    lam2 = 0.87 # ± 0.02 km.w.e.


    resolution = 1000
    thetaRad = np.linspace(0, np.pi/2, resolution)

    #Muon Angular distribution intensity
    meiHime = (I1*np.exp(-slantDepth/(lam1*np.cos(thetaRad)))+I2*np.exp(-slantDepth/(lam2*np.cos(thetaRad))))/np.cos(thetaRad)

    #Defining a random angle
    theta = np.random.choice(np.linspace(thetaRad[0],thetaRad[-1], len(meiHime)),p=meiHime)

    #Constructor
    def __init__(self, position, momentum):
        '''Constructor function for the Muon. Position and Momentum as np arrays in cylindrical coordinates'''
        self.position = position
        self.momentum = momentum

    def getPosition(self):
        '''Returns np.array with cylindrical coordinates'''
        return self.position

    def getMomentum(self):
        '''Returns np.array with cylindrical coordinates'''
        return self.momentum

        #Generic functions for ALL instance of Muon

    @staticmethod
    def getMass():
        '''Mass of the muon; 3-decimal places'''
        return 1.883e-28 #kg

    @staticmethod
    def getCharge():
        '''Charge of the muon; 3-decimal places'''
        return 1.602e-19 #C
