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
