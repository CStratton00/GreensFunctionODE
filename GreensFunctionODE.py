"""
Collin Stratton
CST-305
Topic 3 Project 3: Green's Function and ODE with IVP
Dr. Ricardo Citro

For this project, this is the second part where I am solving the homogeneous from part 1
for both ODEs and plotting the result

Implementation approach:
- developed the dU_dx functions based off the equations in the assignment using scipy.odeint
- developed functions for the green's function solution found in part 1
- created an x space and a y space using odeint and numpy
- graphed the solutions
"""
# Packages used: time, numpy, matplotlib, scipy
import time                         # import time to use for performance analysis
import numpy as np                  # import numpy for array space
import matplotlib.pyplot as plt     # import matplotlib for graphing functions
from scipy.integrate import odeint  # import scipy to use the ordinary differencial equation integral function

# Ordinary Differential Equations
# U is a vector where U[0] = y and U[1] = y'
def dU0_dx(U, x):                           # takes inputs U and x
    return [U[1], -2 * U[1] + 2 * x - 2]    # returns the array of y' and -2y' + 2x -2

def dU1_dx(U, x):                           # takes inputs U and x
    return [U[1], 4 - U[0]]                 # returns the array of y' and 4 - y

# Green's formulas
def green1(x):                              # returns the function of y(x) = 1/2(x^2) - 1.5x - e^(-2x) + 1
    return (0.5 * pow(x, 2)) - (1.5 * x) - (np.exp(-2 * x)) + 1

def green2(x):                              # returns the function of y(x) = 4 - (4 * np.cos(x))
    return 4 - (4 * np.cos(x))

# Time Analysis Variables
ts0, te0, t0 = 0        # time start, end, and summation for the 1st analysis
ts1, te1, t1 = 0        # time start, end, and summation for the 2nd analysis
ts2, te2, t2 = 0        # time start, end, and summation for the 3rd analysis
ts3, te3, t3 = 0        # time start, end, and summation for the 4th analysis

# ODEint solution and
ts0 = time.time()               # time analysis

U0 = [0, 0]                     # vector containing the values of y and y'
xs0 = np.linspace(0, 50, 1000)  # x space from 0-10 with 200 steps
ys0 = odeint(dU0_dx, U0, xs0)   # y space using odeint function to solve the forumla
ys0 = ys0[:,0]                  # cleaning up y space data

te0 = time.time()               # time analysis
t0 = te0 - ts0                  # time summation

ts1 = time.time()               # time analysis

U1 = [0, 0]                     # vector containing the values of y and y'
xs1 = np.linspace(0, 50, 1000)  # x space from 0-10 with 200 steps
ys1 = odeint(dU1_dx, U1, xs1)   # y space using odeint function to solve the forumla
ys1 = ys1[:,0]                  # cleaning up y space data

te1 = time.time()               # time analysis
t1 = te1 - ts1                  # time summation

# Green's Forumla Solution
n = 1000        # initial n value of 1000 chosen
h = 0.05        # initial h value of 0.02 as outlined in the assignment

x0 = 0          # hold variable for x2 space
x1 = 0          # hold variable for x3 space
y0 = 0          # hold variable for y2 space
y1 = 0          # hold variable for y3 space

xs2 = []        # x2 space for green's function
ys2 = []        # y2 space for green's function
xs3 = []        # x3 space for green's function
ys3 = []        # y3 space for green's function

ts2 = time.time()               # time analysis

for i in range(n):  # for loop to run the green function function 200 times
    xs2.append(x0)   # append the x value to the x-space
    ys2.append(y0)  # append the y value to the y-space
    y0 = green1(x0)  # update the y value using the greens function
    x0 += h          # update the x value by moving one step forward (0.05)

te2 = time.time()               # time analysis
t2 = te2-ts2                    # time summation

ts3 = time.time()               # time analysis

for i in range(n):  # for loop to run the green function function 200 times
    xs3.append(x1)   # append the x value to the x-space
    ys3.append(y1)  # append the y value to the y-space
    y1 = green2(x1)  # update the y value using the greens function
    x1 += h          # update the x value by moving one step forward (0.05)

te3 = time.time()               # time analysis
t3 = te3 - ts3                  # time summation


plt.title("(1) ODE and Green's Functions Analysis")     # set the title of the graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs0, ys0, 'r-', label = "ODEint 1", linewidth = 2) # set the ODE line to be red and label it
plt.plot(xs2, ys2, 'b-', label = "Green's Function 1")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # displays the graph

plt.title("(1) ODE Function Analysis")                  # set the title of the graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs0, ys0, 'r-', label = "ODEint 1", linewidth = 2) # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # displays the graph

plt.title("(1) Green's Functions Analysis")             # set the title of the graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs2, ys2, 'b-', label = "Green's Function 1")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()        

plt.title("(2) ODE and Green's Functions Analysis")     # set the title of the graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs1, ys1, 'r-', label = "ODEint 2", linewidth = 2) # set the ODE line to be red and label it
plt.plot(xs3, ys3, 'b-', label = "Green's Function 2")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # displays the graph

plt.title("(2) ODE Function Analysis")                  # set the title of the graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs1, ys1, 'r-', label = "ODEint 2", linewidth = 2) # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # displays the graph

plt.title("(2) Green's Functions Analysis")             # set the title of the graph
plt.xlabel("x")                                             # set the x label on the graph
plt.ylabel("y")                                             # set the y label on the graph
plt.plot(xs3, ys3, 'b-', label = "Green's Function 1")      # set the ODE line to be red and label it
plt.legend()                                                # shows the legend on the graph
plt.show()                                                  # displays the graph

print("Time odeint 1 analysis: " + str(t0))                 # print time for odeint 1
print("Time odeint 2 analysis: " + str(t1))                 # print time for odeint 2

print("Time greens function 1 analysis: " + str(t2))        # print time for greens function 1
print("Time greens function 2 analysis: " + str(t3))        # print time for greens function 2
