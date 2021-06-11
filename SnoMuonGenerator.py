import numpy as np
import scipy as sp
from sp import constants as cst
import SnoMuon as muon

class SnoMuonGenerator(object):
    '''A class for a circular generator of muons located with the overburden of SNOLAB.
            The overburden comes into play with the muon's instantiated directions and energies.

    Attributes:
    **********

    radius   :    the radius of the generator disk (m)
    r        :    position in 3-space -> some kind of array [ x , y , z ] w.r.t the centre
    meiHime  :    the muon intensity w.r.t. the zenith angle, taken from the famous Mei and Hime paper

    '''

    #Number of generated angles
    resolution = 1000
    thetaRad = np.linspace(0,np.pi/2,resolution)

    #Constants for the Mei and Hime function
    slantDepth = 6.011 #km w.e.
    I1 = 8.60e-6 # ± 0.53e-6 /sec/cm^2/sr
    I2 = 0.44e-6 # ± 0.06e-6 /sec/cm^2/sr
    lam1 = 0.45 # ± 0.01 km.w.e.
    lam2 = 0.87 # ± 0.02 km.w.e.

    #Mei and Hime function for muon intensity as a function of zenith angle
    meiHime = (I1*np.exp(-slantDepth/(lam1*np.cos(thetaRad)))+I2*np.exp(-slantDepth/(lam2*np.cos(thetaRad))))/np.cos(thetaRad) # /cm^2/second
    meiHimeNORM = meiHimeIntensity/np.sqrt(np.sum(meiHimeIntensity**2))



    def __init__(self, radius, position):
        self.radius = radius
        self.position = position

    def generateMuons(self, numberOfMuons):
        '''Generates a number of muons at random positions on the Disk
            with zenith angles according to the Mei Hime function and random phi angles
        '''
        muons = np.empty(numberOfMuons)

        for i in range(numberOfMuons):
            muons[i] = SnoMuon()
