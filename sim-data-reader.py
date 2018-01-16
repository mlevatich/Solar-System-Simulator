# Max Levatich
# Solar System Simulation
# Data Reader

import numpy as np
import matplotlib.pyplot as plt
import csv
import math

def convert(data,x):
    '''Converts data to an array of distances from the sun for the planet specified by x'''
    return np.array([math.sqrt(float(data[i][x])**2+float(data[i][x+1])**2)/c for i in range(len(data))])

# Reading the csv into the data list
data = []
with open('data.csv') as f:
    data = [tuple(line) for line in csv.reader(f)]

# Chopping the headers off
data = data[1:]

# Conversion factor to get from meters to AU
c = 149597870700

# Converting data to an array of distances from the sun at each day for each planet
dayscol = np.array([float(data[i][0])/365.25 for i in range(len(data))])
mercury = np.vstack((dayscol,convert(data,1))).T
venus = np.vstack((dayscol,convert(data,3))).T
earth = np.vstack((dayscol,convert(data,5))).T
mars = np.vstack((dayscol,convert(data,7))).T
jupiter = np.vstack((dayscol,convert(data,9))).T
saturn = np.vstack((dayscol,convert(data,11))).T
uranus = np.vstack((dayscol,convert(data,13))).T
neptune = np.vstack((dayscol,convert(data,15))).T

# Plotting data
fig = plt.figure()
fig.suptitle('Planet Orbital Distance')
plt.xlabel('Years')
plt.ylabel('Distance from Sun (AU)')

plt.plot(mercury[:,0],mercury[:,1],label='Mercury')
plt.plot(venus[:,0],venus[:,1],label='Venus')
plt.plot(earth[:,0],earth[:,1],label='Earth')
plt.plot(mars[:,0],mars[:,1],label='Mars')
plt.plot(jupiter[:,0],jupiter[:,1],label='Jupiter')
plt.plot(saturn[:,0],saturn[:,1],label='Saturn')
plt.plot(uranus[:,0],uranus[:,1],label='Uranus')
plt.plot(neptune[:,0],neptune[:,1],label='Neptune')

plt.legend(loc='upper left')
plt.savefig('Data.pdf')
plt.show()
