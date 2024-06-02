import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

print("--- PART 1 ---")

BATMAN = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
NOT_A_BATMAN = np.array([[0,1], [2,3], [5,3], [3,1]])

plt.plot(BATMAN)
plt.show()

plt.plot(NOT_A_BATMAN)
plt.show()

def rotate(array: np.ndarray, angle: int):
    angle = angle*np.pi/180
    i = 0
    for vector in array:
        array[i] = vector @ np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        i+=1
    return array

rot_batman = rotate(BATMAN, 90)
plt.plot(rot_batman)
plt.show()

print("--- PART 2 ---")

