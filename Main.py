from Elements import Muon as mu
from Elements import MuonGenerator as gen
from Elements import Detector as det


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%   Muon Generation for Chroma Simulations  %")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")

# Coordinate system to be based on the detector geometry.
# All elements will take their positions with respect to the instantiated detector


print("Instantiating Detector")

tankRadius = 6.17 #m
tankHeight = 13.0 #m

outerDetector = gen.Generator(tankRadius, tankHeight)





print("Instantiating Generator")
