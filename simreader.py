# Max Levatich, Astro 255
# Solar System Simulation

import numpy as np
import matplotlib.pyplot as plt
import csv
import math
import sys

# Converting earth-alone data to an array of distances from the sun at each day
data = []
c = 149597870700
with open('Jupiter40PercentSun100000.csv') as f:
    data = [tuple(line) for line in csv.reader(f)]
data = data[1:]
dayscol = np.array([float(data[i][0])/365.25 for i in range(len(data))])
mercurycol = np.array([math.sqrt(float(data[i][1])**2+float(data[i][2])**2)/c for i in range(len(data))])
venuscol = np.array([math.sqrt(float(data[i][3])**2+float(data[i][4])**2)/c for i in range(len(data))])
earthcol = np.array([math.sqrt(float(data[i][5])**2+float(data[i][6])**2)/c for i in range(len(data))])
marscol = np.array([math.sqrt(float(data[i][7])**2+float(data[i][8])**2)/c for i in range(len(data))])
jupitercol = np.array([math.sqrt(float(data[i][9])**2+float(data[i][10])**2)/c for i in range(len(data))])
saturncol = np.array([math.sqrt(float(data[i][11])**2+float(data[i][12])**2)/c for i in range(len(data))])
uranuscol = np.array([math.sqrt(float(data[i][13])**2+float(data[i][14])**2)/c for i in range(len(data))])
neptunecol = np.array([math.sqrt(float(data[i][15])**2+float(data[i][16])**2)/c for i in range(len(data))])
mercury = np.vstack((dayscol,mercurycol)).T
venus = np.vstack((dayscol,venuscol)).T
earth = np.vstack((dayscol,earthcol)).T
mars = np.vstack((dayscol,marscol)).T
jupiter = np.vstack((dayscol,jupitercol)).T
saturn = np.vstack((dayscol,saturncol)).T
uranus = np.vstack((dayscol,uranuscol)).T
neptune = np.vstack((dayscol,neptunecol)).T
'''
fig = plt.figure()
fig.suptitle('Stability of Earth\'s Orbit Over 100,000yrs')
plt.xlabel('Mass of Jupiter (Solar Masses)')
plt.ylabel('Perihelion of Jupiter (AU)')
msize = 8
a, = plt.plot(3, 0.735364453632, marker='o', markersize=msize, color='red', label='Earth Ejected')
plt.plot(2, 1.02788528006, marker='o', markersize=msize, color='red')
plt.plot(1, 1.69290367338, marker='o', markersize=msize, color='red')
plt.plot(0.5, 2.53303614874, marker='o', markersize=msize, color='red')
plt.plot(0.45, 2.65621081352, marker='o', markersize=msize, color='red')
plt.plot(0.4, 2.80716933559, marker='o', markersize=msize, color='red')
b, = plt.plot(0.35, 2.96809777443, marker='o', markersize=msize, color='blue', label = 'Stable')
plt.plot(0.3, 3.14987936575, marker='o', markersize=msize, color='blue')
plt.plot(0.25, 3.34948723159, marker='o', markersize=msize, color='blue')
plt.plot(0.1, 4.15670044368, marker='o', markersize=msize, color='blue')
plt.legend(handles=[a,b])
plt.savefig('FINAL_PLOTDOWN.pdf')
# plt.show()
sys.exit(0)
'''

# Plotting data
fig = plt.figure()
fig.suptitle('Planet Orbital Distance\nJupiter = 0.4 Solar Masses')
plt.xlabel('Years')
plt.ylabel('Distance from Sun (AU)')

# plt.axhline(1)
plt.axis([0,2000,0,70])

plt.plot(mercury[:,0],mercury[:,1],label='Mercury')
plt.plot(venus[:,0],venus[:,1],label='Venus')
plt.plot(earth[:,0],earth[:,1],label='Earth')
plt.plot(mars[:,0],mars[:,1],label='Mars')
plt.plot(jupiter[:,0],jupiter[:,1],label='Jupiter')
plt.plot(saturn[:,0],saturn[:,1],label='Saturn')
plt.plot(uranus[:,0],uranus[:,1],label='Uranus')
plt.plot(neptune[:,0],neptune[:,1],label='Neptune')

plt.legend(loc='upper left')
plt.savefig('Jupiter40.pdf')
# plt.show()
