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

assets = [sun , planet]

#Newton attraction

#Constant universal Gravity
G = 1

def calc_acceleration(body, attractor):

	#Calculate vector distance, then convert vector to num
	distance = body.pos - attractor.pos
	d = np.linalg.norm(distance)
	
	# G(mass1 * mass2)
	numerator = G * body.mass * attractor.mass

	denominator = np.power(d , 2)
	force = numerator / denominator

	magnitude = force / body.mass
	direction - distance / d
	acceleratation = magnitude * direction

	return acceleration

#Function Main
tick = 0.1

#for i in range

#Draw on screen
axet = 10

#environment, Cartesian plane
fig, ax = plt.subplots(figsize=(10 , 10))
ax.set_xlim(-axet , axet)
ax.set_ylim(-axet , axet)
ax.set_aspect('equal')
ax.set_title('Orbital system')

circles = []
for asset in assets:
	colour =
	size =


plt.show()