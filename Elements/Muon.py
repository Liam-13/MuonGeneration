####################################################
#                    Muon Class                    #
#        Muon Class for Storing Attributes         #
#               And Distribution Data              #
####################################################


import numpy as np
import scipy.constants as cst

class SnoMuon(object):
    '''The Muon class for our favourite particle to veto. Attenuated by the SNOLAB overburden.

    Attributes:
    **********

    charge   :    the elementary charge -> from CODATA
    mass     :    ordinary mass of muons -> from CODATA
    r        :    position in 3-space -> some kind of array [ x , y , z ]
    energy   :    due to attenuation in the overburden, muon energy is random, but not totally.
    dir      :    direction of Muon propagation
    mom      :    momentum in 3-space -> some kind of array

    '''

    #All muons have:

    mass = cst.value('muon mass') #From CODATA
    charge = cst.e #From CODATA

    #For random choices
    angleResolution = 1000
    phis = np.linspace(0,np.pi*2,angleResolution) #Arbitrary resolution at 1000 different angles

    #Zenith angle distribution according to Mei and Hime 2004



    def __init__(self, initial_position, theta, energy = 1.0, phi = np.random.choice(phis)):
        '''Built to initialize a muon with a position, energy and direction
            dictated by the two angles of spherical coordinates
        '''

        #Basic assignment of initial position
        self.r = initial_position
        self.theta = theta
        self.energy = energy
        self.phi = phi  #Radially symmetric




### Generic Methods ###

def mass():
    '''Returns CODATA Muon Mass from Scipy Package'''
    return cst.value('muon mass')

def charge():
    '''Returns CODATA elementary charge from Scipy Package '''
    return cst.e
