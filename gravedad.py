import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#class for 3 entities
#elements: mass, position, velocity
class Body:
	def __init__(self, name, mass, pos, vel):
		self.name = name
		self.mass = mass
		self.pos = pos
		self.vel = vel


#entity sun, planet and rocket
sun = Body("Sun", 10000.0, np.array([0.0 , 0.0]), np.array([0.0 , 0.0]))
planet = Body("Planet", 1000.0, np.array([10.0 , 0.0]), np.array([0.0 , 8.0]))
#rocket = Body("Rocket", 1.0, np.array([10.0 , 0.0]), np.array([0.0 , 8.0]))

#Newton Gravity
def calc_aceleration(body, attractor):
	Planet
	Sun

#Function Main
tick = 0.1

#for i in range

#Draw on screen