import numpy as np
import scipy as sp
from sp import constants as cst

class SnoMuonGenerator(object):
    '''A generator class to create muons with positions and momenta according to their
        distribution functions at SNOLAB.

    Attributes:
    **********

    charge   :    the elementary charge -> from CODATA
    mass     :    ordinary mass of muons -> from CODATA
    r        :    position in 3-space -> some kind of array [ x , y , z ]
    energy   :    due to attenuation in the overburden, muon energy is random, but not totally.
    mom      :    momentum in 3-space -> some kind of array

    '''
