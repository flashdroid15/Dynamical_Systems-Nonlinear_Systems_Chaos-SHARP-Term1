import numpy as np
import matplotlib.pyplot as plt

# Defining constants
s, r, b = 10, 28, (8/3)
s, r, b = float(s), float(r), float(b)

def x_dot(x, y, z, t):
    return ( s * (y - x) )

def y_dot(x, y, z, t):
    return ( (r*x) - y - (x*z) )

def z_dot(x, y, z, t):
    return ( (x*y) - (b*z) )

# choose a different color for each trajectory
# colors = plt.cm.viridis(np.linspace(0, 1, 10))
def lorenz_2D_plot(x, y, z):
    #plt.figure(figsize = (8.5,8.5))

    #plt.plot(t, x, color = 'r') 
    plt.plot(t, y, color = 'g')
    #plt.plot(t, z, color = 'b')

    plt.grid(True)

    plt.xlabel('Time --->')
    plt.ylabel('y --->')
    plt.title('Case 1')
    
    plt.show()
    return 

def RK(x_dot,y_dot,z_dot):
    # Max Time and Intervals
    T, n = 70, 7000
    T, n = float(T), int(n)

    # The independent variable
    t = np.zeros(n+1)

    # The dependent variables
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    z = np.zeros(n+1)
    
    # Setting initial conditions
    t[0] = 0
    x[0] = 0
    y[0] = 1
    z[0] = 0
    
    h = T / n 
    
    # Iterations
    for K in range(0, n):
    
        t[K+1] = t[K] + h
        
        xK1 = x_dot(x[K], y[K], z[K], t[K])
        yK1 = y_dot(x[K], y[K], z[K], t[K])
        zK1 = z_dot(x[K], y[K], z[K], t[K])

        xK2 = x_dot((x[K] + 0.5*xK1*h), (y[K] + 0.5*yK1*h), (z[K] + 0.5*zK1*h), (t[K] + h/2))
        yK2 = y_dot((x[K] + 0.5*xK1*h), (y[K] + 0.5*yK1*h), (z[K] + 0.5*zK1*h), (t[K] + h/2))
        zK2 = z_dot((x[K] + 0.5*xK1*h), (y[K] + 0.5*yK1*h), (z[K] + 0.5*zK1*h), (t[K] + h/2))

        xK3 = x_dot((x[K] + 0.5*xK2*h), (y[K] + 0.5*yK2*h), (z[K] + 0.5*zK2*h), (t[K] + h/2))
        yK3 = y_dot((x[K] + 0.5*xK2*h), (y[K] + 0.5*yK2*h), (z[K] + 0.5*zK2*h), (t[K] + h/2))
        zK3 = z_dot((x[K] + 0.5*xK2*h), (y[K] + 0.5*yK2*h), (z[K] + 0.5*zK2*h), (t[K] + h/2))

        xK4 = x_dot((x[K] + xK3*h), (y[K] + yK3*h), (z[K] + zK3*h), (t[K] + h))
        yK4 = y_dot((x[K] + xK3*h), (y[K] + yK3*h), (z[K] + zK3*h), (t[K] + h))
        zK4 = z_dot((x[K] + xK3*h), (y[K] + yK3*h), (z[K] + zK3*h), (t[K] + h))

        x[K+1] = x[K] + (h*(xK1 + 2*xK2 + 2*xK3 + xK4) / 6)
        y[K+1] = y[K] + (h*(yK1 + 2*yK2 + 2*yK3 + yK4) / 6)
        z[K+1] = z[K] + (h*(zK1 + 2*zK2 + 2*zK3 + zK4) / 6)

    return x, y, z, t

x, y, z, t = RK(x_dot,y_dot,z_dot)

lorenz_2D_plot(x,y,z)