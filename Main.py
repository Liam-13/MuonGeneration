import numpy as np
from Elements import Muon as mu
from Elements import Generator as gen
from Elements import Detector as det


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%   Muon Generation for Chroma Simulations  %")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")

# Coordinate system to be based on the detector geometry.
# All elements will take their positions with respect to the instantiated detector

### Detector Parameters ###
OD_Radius = 6.1722 #m
OD_Height = 13.300 #m
OD_Position = np.array([0.,0.,0.])
#Instantiation
print("Instantiating Detector:")
OD = det.Detector(OD_Radius, OD_Height, "nEXO_OD", OD_Position) #Position at Center
print(str(OD))


### Generator Parameters ###
Gen_Radius = 100 #m
Gen_Position = np.array([0.,0.,20.0 + OD_Height/2]) #20 m above Detector
#Instantiation
print("Instantiating Generator:")
MuonGen = gen.Generator(Gen_Radius, Gen_Position)
print(str(MuonGen))


### Generate Muons ###
numMuons = 10

muons = MuonGen.generateMuons(numMuons)

for i in range(numMuons):
    print(str(muons[i]))
