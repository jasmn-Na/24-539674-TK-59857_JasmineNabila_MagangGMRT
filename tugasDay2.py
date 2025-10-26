import numpy as np
import math
import matplotlib.pyplot as plt

print('24/539674/TK/59857 Jasmine Nabila')
print()
print('Panjang femur: 74, Panjang tibia: 57')
print('besar sudut 1: 40 derajat, dan besar sudut 2: 30 derajat')

L1 = 74
L2 = 57
Teta1 = math.radians(40)
Teta2 = math.radians(30)

X = L1*math.cos(Teta1) + L2*math.cos(Teta1 + Teta2)
Y = L1*math.sin(Teta1) + L2*math.sin(Teta1 + Teta2)

print()
print('X =', round(X, 2))
print('Y =', round(Y, 2))

#posisi ujung femur
X1 = L1*math.cos(Teta1)
Y1 = L1*math.sin(Teta2)

#posisi ujung tibia
X2 = X1 + L1*math.cos(Teta1 + Teta2)
Y2 = Y1 + L1*math.sin(Teta1 + Teta2)
print(f"posisi ujung femur :{round(X1, 2), round(Y1, 2)}")
print(f"posisi ujung tibia :{round(X2, 2), round(Y2, 2)}")
print()

femurX = np.array([0, X1])
femurY = np.array([0, Y1])

tibiaX = np.array([X1, X2])
tibiaY = np.array([Y1, Y2])

print()
plt.plot(femurX, femurY, label='femur')
plt.plot(femurX, femurY, 'o', color='black')
plt.plot(tibiaX, tibiaY, label='tabia')
plt.gca().invert_xaxis()  
plt.gca().invert_yaxis()
plt.xlabel('posisi x')
plt.ylabel('posisi y')
plt.title('Forward Kinematics 2 DoF')
plt.legend()
plt.grid(True)
plt.show()