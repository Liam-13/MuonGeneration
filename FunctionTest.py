import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt


class MuonDist(st.rv_continuous):
    """Muon Angular Distribution PDF"""
    def _pdf(self, theta):
        slantDepth = 6.011 #km w.e.
        I1 = 8.60e-6 # ± 0.53e-6 /sec/cm^2/sr
        I2 = 0.44e-6 # ± 0.06e-6 /sec/cm^2/sr
        lam1 = 0.45 # ± 0.01 km.w.e.
        lam2 = 0.87 # ± 0.02 km.w.e.
        return (I1*np.exp(-slantDepth/(lam1*np.cos(theta)))+I2*np.exp(-slantDepth/(lam2*np.cos(theta))))/np.cos(theta) # /cm^2/second

function = MuonDist(a=0, b=np.pi/2, name = 'Muon Distribution')

for i in range(100):
    print(function.rvs())
