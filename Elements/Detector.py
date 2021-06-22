import numpy as np
import scipy as sp
from sp import constants as cst


class Detector(object):
    '''A rudimentary class for a cylindrical detector'''


    def __init__(self, radius, height, position = np.array([0.,0.,0.])):

        self.radius = radius
        self.height = height
        self.position = position

        self.fill = "Water"
        self.slantDepth = 6.011 #km w.e.

    
