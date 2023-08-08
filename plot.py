import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


q1 = float(input("Enter the value of charge 1 (in Coulombs): "))
q2 = float(input("Enter the value of charge 2 (in Coulombs): "))
r1 = np.array([2, 0, 1])
r2 = np.array([1, 0, 4])
r = r2 - r1

#
def animate():
    global r1, r2, F
    unit_vector = make_unit_vector(r)
    distance = math.sqrt(r[0]**2 +r[1]**2 +r[2]**2)

    
    k = 8.99e9  
    magnitude =  k* (q1 * q2) /(distance ** 2)
    force_vector = magnitude *unit_vector 
    #print(distance)
    print("magnitude : %f" %(magnitude))
    print("vector :",force_vector)
    return force_vector

def make_unit_vector(vector):
    
    magnitude = np.linalg.norm(vector)  
    if magnitude == 0:
        return vector  
    return vector / magnitude

   
vector= animate()
print(vec)
ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='b')

ax.set_xlim([0, vector[0] + 1])
ax.set_ylim([0, vector[1] + 1])
ax.set_zlim([0, vector[2] + 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(r1[0], r1[1], r1[2], color='r', s=100)
ax.scatter(r2[0], r2[1], r2[2], color='b', s=100)

ax.quiver(r2[0], r2[1], r2[2], vector[0], vector[1], vector[2], color='g')
plt.show()
