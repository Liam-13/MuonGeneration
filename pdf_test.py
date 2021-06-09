import numpy as np


slantDepth = 6.011 #km w.e.
I1 = 8.60e-6 # ± 0.53e-6 /sec/cm^2/sr
I2 = 0.44e-6 # ± 0.06e-6 /sec/cm^2/sr
lam1 = 0.45 # ± 0.01 km.w.e.
lam2 = 0.87 # ± 0.02 km.w.e.



resolution = 1000
thetaRad = np.linspace(0, np.pi/2, resolution)

#Muon Angular distribution intensity
meiHime = (I1*np.exp(-slantDepth/(lam1*np.cos(thetaRad)))+I2*np.exp(-slantDepth/(lam2*np.cos(thetaRad))))/np.cos(thetaRad)

meiHime = meiHime / np.sqrt(meiHime.sum()**2) #Normalizes the mei hime distribution function

#Defining a random angle
theta = np.random.choice(np.linspace(thetaRad[0],thetaRad[-1], len(meiHime)),p=meiHime)


print(theta)
