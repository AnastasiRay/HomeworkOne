import numpy as np
import matplotlib.pyplot as plt

with open('examp16.txt') as log:
    data = log.readlines()

lidar_position = 0.3
search_angle = 240
searches_nums = 681
step = search_angle / searches_nums

plt.figure(figsize=(20, 20))

for row in data[-10:]:
    odom, lidar = row.split(';')
    odom = list(map(float, odom.split(', ')))
    lidar = list(map(float, lidar.split(', ')))

    plt.scatter(odom[0], odom[1], color='red', s=1)
    lidar_x = odom[0] + lidar_position * np.cos(odom[2])
    lidar_y = - odom[1] + lidar_position * np.sin(odom[2])

    for i, distance in enumerate(lidar):
        angle = np.radians(step * i) - odom[2] - np.radians(120)
        obj_x = lidar_x + distance * np.cos(angle)
        obj_y = lidar_y + distance * np.sin(angle)
        plt.scatter(obj_x, obj_y, color='blue', s=1)

plt.show()