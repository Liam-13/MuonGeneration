import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Detector:
    fill = "Water"  #Might be useful later
    radius = 0.
    height = 0.
    name = "Cylindrical Detector"
    centre = np.array([0.,0.,0.])
    slantDepth =  6.0110 #km.w.e.


    def __init__(self, radius, height, depth):
        '''Constructor takes detector dimensions and slant depth'''
        self.radius = radius
        self.height = height
        self.slantDepth = depth #km.w.e.

        #Takes the coordinate values
    def setCentre(self, rho, theta, z):
        #in Cylindrical coordinates
        self.centre[0] = rho
        self.centre[1] = theta
        self.centre[2] = z

        #Takes a list argument or np. array
    def setCentre(self, coords):
        self.centre[0] = coords[0]
        self.centre[1] = coords[1]
        self.centre[2] = coords[2]

    def volume(self):
        circ = np.pi*(self.radius**2)
        return circ*self.height

    def inDetector(self, coords):
        '''A test method that returns True if the given coordinates are in the detector, False otherwise
            takes argument coords meant to be array or list of coordinates
        '''

        #Minimum and Maximum values for coordinates
        zmin = -0.5*self.height + centre[2]
        zmax = 0.5*self.height + centre[2]

        xmin = -self.radius + centre[0]
        xmax = self.radius + centre[0]

        ymin = -self.radius + centre[1]
        ymax = self.radius + centre[1]

        x_coord = coords[0]*np.cos(coords[1])
        y_coord = coords[0]*np.sin(coords[1])

        #is above or below?
        if coords[2] > zmax or coords[2] < zmin:
            return False

        #is out of x range?
        elif x_coord > xmax or x_coord < xmin:
            return False

        #is out of y range?
        elif y_coord > ymax or y_coord < ymin:
            return False

        #is in the detector.
        else:
            return True


        #Shows a 3D plot of the Detector volume
    def detectorPlot(self, res):
        fig = plt.figure()

        xlim = self.radius + self.centre[0]
        zmin = -0.5*self.height + self.centre[2]
        zmax = 0.5*self.height + self.centre[2]

        # Plotting the Cylindrical Detector

        z = np.linspace(zmin, zmax, res)
        theta = np.linspace(0, 2*np.pi, res)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x_grid = self.radius*np.cos(theta_grid) + self.centre[0]
        y_grid = self.radius*np.sin(theta_grid) + self.centre[1]

        ax = fig.add_subplot(111, projection='3d')
        Xc,Yc,Zc = x_grid, y_grid, z_grid

        ax.plot_surface(Xc, Yc, Zc, alpha = 0.5)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        title = 'Detector Volume at', self.slantDepth, ' km w.e.'

        ax.set_title(title)
        #plt.savefig("DETECTOR.png")
        plt.show()

    def areaAtAngle(self, theta):
        '''Returns the cross-sectional area of the detector with a plane at zenith angle theta, m^2'''
        top = np.pi*self.radius**2
        side = 2*self.radius*self.height

        area = np.cos(theta)*top + np.sin(theta)*side

        return area


    def meiHime(theta):
        '''Returns the anticipated Muon Flux from one angle theta at slant depth 6.011 km.w.e. according to the Mei and Hime paper'''

        #Defining constants
        slantDepth = 6.011 #km w.e.
        I1 = 8.60e-6 # ± 0.53e-6 /sec/cm^2/sr
        I2 = 0.44e-6 # ± 0.06e-6 /sec/cm^2/sr
        lam1 = 0.45 # ± 0.01 km.w.e.
        lam2 = 0.87 # ± 0.02 km.w.e.

        meiHime = np.sin(theta)*(I1*np.exp(-slantDepth/(lam1*np.cos(theta)))+I2*np.exp(-slantDepth/(lam2*np.cos(theta))))/np.cos(theta) # /cm^2/second
        meiHime = meiHime /np.sqrt(np.sum(meiHime)**2.0)

        return meiHime
