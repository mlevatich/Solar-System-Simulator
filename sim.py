# Max Levatich
# Solar System Simulation

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import sys
import csv

def step():
    # Update positions
    state[:, 0:2] += dt * state[:, 2:4]

    # For each planet 'i',
    # modify velocity due to gravitational force from all planets
    planets = range(len(state))
    for i in planets:
        # Mass of current planet
        mass = state[i,4]

        # X and Y distances to all other planets
        x_distances = state[:,0] - state[i,0]
        y_distances = state[:,1] - state[i,1]

        # Distances to all other planets
        distance_to = np.sqrt(x_distances**2 + y_distances**2)

        # Setting current object to be infinitely far away, removing it
        distance_to[i] = np.inf

        # Calculating gravitational force from all other planets
        vector_force_from = (G * mass * state[:,4]) / np.square(distance_to)

        # Splitting forces into x and y components for each planet
        x_force_from = vector_force_from * x_distances / distance_to
        y_force_from = vector_force_from * y_distances / distance_to

        # Summing the forces and calculating x and y acceleration
        x_accel = sum(x_force_from) / mass
        y_accel = sum(y_force_from) / mass

        # Changing velocity
        state[i,2] += x_accel * dt
        state[i,3] += y_accel * dt

# PROGRAM RUN STARTS HERE
state = np.asarray([[],], dtype=float)
timeclocked = 0
G = 6.67408e-11
dt = 43200

# Initial coordinates
sun =       np.array([299570984, 890176321, -9.64222754, 9.1001829, 1.989e30])
mercury =   np.array([54139325892, -7487456797, -1948.053578, 50324.603, 0.33e24])
venus =     np.array([-82595933266, -68518586571, 22224.66627, -27007.628855, 4.87e24])
earth =     np.array([63420611195, 134334517611, -27425.86697, 12625.103938, 5.972e24])
mars =      np.array([-246877701719, 9084926253, 92.3955417, -22136.927327, 0.64171e24])
jupiter =   np.array([-660489093226, -473131360991, 7455.0025798, -10000.149431, 1898.19e24])
saturn =    np.array([-20439865549, -1504285458099, 9128.19025, -161.247279, 568.34e24])
uranus =    np.array([2660831834805, 1338399627747, -3109.861725, 5766.2331133, 86.813e24])
neptune =   np.array([4286074199355, -1301127800528, 1543.183456, 5232.8797883, 102.413e24])

# Setting up figure and animation
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
fig.patch.set_facecolor('black')

# Giving initial state
if len(sys.argv) > 1 and sys.argv[1] == 'custom':
    state = np.array([sun, mercury, venus, earth, mars, jupiter])
    mercury_orbit = patches.Circle([0,0],radius=57.9e9,edgecolor='w',facecolor='none')
    ax.add_patch(mercury_orbit)
    venus_orbit = patches.Circle([0,0],radius=108.2e9,edgecolor='w',facecolor='none')
    ax.add_patch(venus_orbit)
    earth_orbit = patches.Circle([0,0],radius=1.496e11,edgecolor='w',facecolor='none')
    ax.add_patch(earth_orbit)
    mars_orbit = patches.Circle([0,0],radius=2.2892e11,edgecolor='w',facecolor='none')
    ax.add_patch(mars_orbit)
    jupiter_orbit = patches.Circle([0,0],radius=7.7857e11,edgecolor='w',facecolor='none')
    ax.add_patch(jupiter_orbit)
elif len(sys.argv) > 1 and sys.argv[1] == 'inner':
    state = np.array([sun, mercury, venus, earth, mars])
    mercury_orbit = patches.Circle([0,0],radius=57.9e9,edgecolor='w',facecolor='none')
    ax.add_patch(mercury_orbit)
    venus_orbit = patches.Circle([0,0],radius=108.2e9,edgecolor='w',facecolor='none')
    ax.add_patch(venus_orbit)
    earth_orbit = patches.Circle([0,0],radius=1.496e11,edgecolor='w',facecolor='none')
    ax.add_patch(earth_orbit)
    mars_orbit = patches.Circle([0,0],radius=2.2892e11,edgecolor='w',facecolor='none')
    ax.add_patch(mars_orbit)
elif len(sys.argv) > 1 and sys.argv[1] == 'earth':
    state = np.array([sun,earth])
    earth_orbit = patches.Circle([0,0],radius=1.496e11,edgecolor='w',facecolor='none')
    ax.add_patch(earth_orbit)
else:
    state = np.array([sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune])
    mercury_orbit = patches.Circle([0,0],radius=57.9e9,edgecolor='w',facecolor='none')
    ax.add_patch(mercury_orbit)
    venus_orbit = patches.Circle([0,0],radius=108.2e9,edgecolor='w',facecolor='none')
    ax.add_patch(venus_orbit)
    earth_orbit = patches.Circle([0,0],radius=1.496e11,edgecolor='w',facecolor='none')
    ax.add_patch(earth_orbit)
    mars_orbit = patches.Circle([0,0],radius=2.2792e11,edgecolor='w',facecolor='none')
    ax.add_patch(mars_orbit)
    jupiter_orbit = patches.Circle([0,0],radius=7.7857e11,edgecolor='w',facecolor='none')
    ax.add_patch(jupiter_orbit)
    saturn_orbit = patches.Circle([0,0],radius=14.3353e11,edgecolor='w',facecolor='none')
    ax.add_patch(saturn_orbit)
    uranus_orbit = patches.Circle([0,0],radius=28.7246e11,edgecolor='w',facecolor='none')
    ax.add_patch(uranus_orbit)
    neptune_orbit = patches.Circle([0,0],radius=44.9506e11,edgecolor='w',facecolor='none')
    ax.add_patch(neptune_orbit)

plt.axis('off')
plt.axis([-45e11,45e11,-45e11,45e11])

# Holds the locations of the planets
planets, = ax.plot([], [], 'bo', ms=6)
planets.set_markersize(10)

# Text to keep track of elapsed time
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color = 'w')

# Global variable
record = []

# GETS SIMULATION DATA, NO ANIMATION
for j in range(730000*100):
    step()
    timeclocked += dt
    if j % 1000 == 0:
        print(j)
        days = (timeclocked*1.15741e-5)
        record.append((days,state[1,0]-state[0,0],state[1,1]-state[0,1],
                            state[2,0]-state[0,0],state[2,1]-state[0,1],
                            state[3,0]-state[0,0],state[3,1]-state[0,1],
                            state[4,0]-state[0,0],state[4,1]-state[0,1],
                            state[5,0]-state[0,0],state[5,1]-state[0,1],
                            state[6,0]-state[0,0],state[6,1]-state[0,1],
                            state[7,0]-state[0,0],state[7,1]-state[0,1],
                            state[8,0]-state[0,0],state[8,1]-state[0,1],))
with open('Jupiter100PercentSun100000.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['Days','mercury-x','mercury-y','venus-x','venus-y','earth-x','earth-y',
                    'mars-x','mars-y','jupiter-x','jupiter-y','saturn-x','saturn-y',
                    'uranus-x','uranus-y','neptune-x','neptune-y',])
    for row in record:
        csv_out.writerow(row)
sys.exit(0)

# This initializes the animation
def init():
    planets.set_data([], [])
    time_text.set_text('')
    return planets,

# This performs one step of the animation
def animate(i):
    global ax, fig, timeclocked, state, dt
    step()
    timeclocked += dt
    years = (timeclocked / 31536e3)
    planets.set_data(state[:, 0], state[:, 1])
    time_text.set_text('%d years' % years)
    plt.axis([-45e11+state[0,0],45e11+state[0,0],-45e11+state[0,1],45e11+state[0,1]])
    return planets, time_text, ax

# Animation!
ani = animation.FuncAnimation(fig, animate, frames=600, interval=1,
                                blit=True, init_func=init)
plt.show()
