import numpy
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def SEIRD_Equations(Population, t):
    S, E, I, R, D = Population

    # Constants
    rB = 0.8
    epsilon = 0.2
    gamma = 0.1
    delta = 0.05

    N = S + E + I + R + D
    dS_dt = -rB * S * I / N
    dE_dt = (rB * I / N) * S - (epsilon * E)
    dI_dt = epsilon * E - (gamma * I) - (delta * I)
    dR_dt = gamma * I
    dD_dt = delta * I
    return dS_dt, dE_dt, dI_dt, dR_dt, dD_dt

# Initial Conditions
S0 = 999
E0 = 0
I0 = 1
R0 = 0
D0 = 0
Population0 = S0, E0, I0, R0, D0

# Measurement of time in days
t = numpy.linspace(0, 366, 366)

SEIRD_Model = odeint(SEIRD_Equations, Population0, t)

S, E, I, R, D = SEIRD_Model.T

def SEIRD_Plot(t, S, E, I, R, D):
    N = S + E + I + R + D
    
    plt.plot(t, S, label="Susceptible")
    plt.plot(t, E, label="Exposed")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Recovered")
    plt.plot(t, D, label="Died")
    plt.plot(t, N, label="Total")

    plt.legend()

    plt.xlabel("Time (days) ===>")
    plt.ylabel("Number of People ===>")

    plt.show()
    return

SEIRD_Plot(t, S, E, I, R, D)

print( "The number of infected individuals peak at", max(I), "at Day", numpy.argmax(I) )

def Infected_10(array):
    Forward = list(range(1, (array.size)+1))
    Backward = [-x for x in Forward] # Makes it an array
    for i in Backward:
        if I[i] >= 10:
            value = i+366 # since i is negative
            return value

print( "There are 10 Infected people left remaining at Day ", Infected_10(I) )