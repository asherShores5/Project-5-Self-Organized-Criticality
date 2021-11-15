#Asher Shores
#Dr. Ricardo Citro
#This is my own work

#Differential Equations:
# x' = o(y-x)
# y' rx - y - xz
# z' xy - bz

#Implementation
#Use lorenz lib methods to create and solve differential equations.
#Solve dy/dx compare results.

import numpy as np                  #import lib numpy as np for math
import matplotlib.pyplot as plt     #import lib matplotlib to graph
from mpl_toolkits.mplot3d import Axes3D #import the 3d plot thingy

#Set values for s, r, and b as given in documentation
#Return x,y,z-dot values for partials at point x, y, z

def lorenz(x, y, z, s=10, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

#Plots
def plots(r):
    #here we define the 2d and 3d projection figures to map onto
    fig = plt.figure(1)
    ax = fig.gca(projection='3d')

    ax.plot(xs, ys, zs, lw=0.5)            #plot given points
    ax.set_xlabel("X Axis")                #x-axis label
    ax.set_ylabel("Y Axis")                #y-axis label
    ax.set_zlabel("Z Axis")                #z-axis label
    ax.set_title("Lorenz Attractor, r = 28")#set title
    plt.show()          #plot the plot

    #new plot for x/t
    plt.title("x/t")    #new title
    plt.xlabel("t")     #label horz t
    plt.ylabel("x")     #label vert x
    plt.plot(ts, xs)    #plot the plot
    plt.legend          #legend
    plt.show()          #shows it

    #new plot y/t
    plt.title("y/t")    #new title
    plt.xlabel("t")     #label horz t
    plt.ylabel("y")     #label vert y
    plt.plot(ts, ys)    #plot the plot
    plt.legend          #legend
    plt.show()          #shows it

    #new plot z/t
    plt.title("z/t")    #new title
    plt.xlabel("t")     #label horz t
    plt.ylabel("z")     #label vert z
    plt.plot(ts, zs)    #plot the plot
    plt.legend          #legend
    plt.show()          #shows it

dt = 0.01           #step size
num_steps = 10000   #number of steps
#these were standard not chosen

#Need one more for the initial values
xs = np.empty(num_steps + 1)            #creating an empty x space
ys = np.empty(num_steps + 1)            #creating an empty y space
zs = np.empty(num_steps + 1)            #creating an empty z space
ts = np.linspace(0, 100, num_steps + 1) #creating an empty t space

#setting initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

#Step through "time", calculating the partial derivatives at the current point and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], 10, 28, 2.667) #using s = 10, r = 28, and b = 8/3
    xs[i + 1] = xs[i] + (x_dot * dt)                                #filling xs
    ys[i + 1] = ys[i] + (y_dot * dt)                                #filling ys
    zs[i + 1] = zs[i] + (z_dot * dt)                                #filling zs

plots(5)
