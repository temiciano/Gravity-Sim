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
sun = Body("Sun", 1000.0, np.array([0.0 , 0.0]), np.array([0.0 , 0.0]))
planet = Body("Planet", 10.0, np.array([12.0 , 0.0]), np.array([0.0 , 5.0]))
#rocket = Body("Rocket", 1.0, np.array([10.0 , 0.0]), np.array([0.0 , 8.0]))

assets = [sun , planet]

#Newton attraction

#Constant universal Gravity
G = 1

def calc_acceleration(body, attractor):

	#Calculate vector distance, then convert vector to num
	distance = body.pos - attractor.pos
	r = np.linalg.norm(distance)
	
	# G(mass1 * mass2)
	numerator = G * body.mass * attractor.mass

	denominator = r**2
	force = numerator / denominator

	magnitude_accel = force / body.mass
	direction = -distance / r
	acceleration = magnitude_accel * direction

	return acceleration

#Function Main
tick = 0.01

#Draw on screen
axet = 15

#environment, Cartesian plane
fig, ax = plt.subplots(figsize=(10 , 10))
ax.set_xlim(-axet , axet)
ax.set_ylim(-axet , axet)
ax.set_aspect('equal')
ax.set_title('Orbital system')

points = []
for asset in assets:
	colour = 'yellow' if asset.name == "Sun" else 'lightblue'
	size = 100 if asset.name == "Sun" else 20
	p, = ax.plot([], [], 'o', color=colour, markersize=size)
	points.append(p)

def refresh(frame):
	a = calc_acceleration(planet, sun)
	planet.vel = planet.vel + a * tick
	planet.pos = planet.pos + planet.vel * tick

	for point, asset in zip(points, assets):
		point.set_data([asset.pos[0]], [asset.pos[1]])

	return points


sim = animation.FuncAnimation(fig, refresh, frames=2000, interval=10, blit=True)
plt.show()