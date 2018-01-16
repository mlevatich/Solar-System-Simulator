# Solar-System-Simulator
This project consists of two executable python files: the first generates positional data for planets in the solar system up to 1 million years in the future and writes it to a csv file.  The second reads the csv file and displays the planets' positions over time as a plot.

# The Simulation
The initial positions of all the planets were gathered from barycentric ephemerides generated by the JPL Horizons web interface. Motion is simulated via numerical integration – forces from all other planets are calculated after every timestep and the planets' velocities are adjusted accordingly.  The time resolution is configurable, but is set to a default of 12 hour timesteps (far more than enough to guarantee total accuracy of data). A lower time resolution means less accurate data but faster data collection – it takes the program a few days of real time to collect a million years of simulated data with a 12 hour timestep.

# Usage
Running sim-run.py generates the planetary data and writes it to a csv file called data.csv.  Running sim-data-reader.py reads that data and saves a pdf plot of planetary positions over time. sim-run.py cannot be called with any command line arguments, but a user can easily configure the mass, position, and number of planets from within the file. A rudimentary animation can also be switched on, though it is currently commented out because it massively slows down data collection.

# Poster
I used this program for a astronomical research project, the final poster for which I have included in this repository, in case anyone is curious about potential uses of the program.
