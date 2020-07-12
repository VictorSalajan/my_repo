import random
import matplotlib.pylab as plt

def drunkard_walk(k=100000):
    """ returns the average distance a drunken walk
    will be from the origin. k = steps"""
    x = ['x-axis', 0]
    y = ['y-axis', 0]
    path_on_x = [x[1]]
    path_on_y = [y[1]]
    for _ in range(k):
        random_axis = random.choice([x, y])
        if x == random_axis:
            x[1] += random.choice([1, -1])
            path_on_x.append(x[1])
            path_on_y.append(y[1])
        else:
            y[1] += random.choice([1, -1])
            path_on_x.append(x[1])
            path_on_y.append(y[1])
    return x[1], y[1], path_on_x, path_on_y


all_distances = [[], []]
x_paths = []
y_paths = []
k = 100000
n = 10
for _ in range(n):
    sim = drunkard_walk(k)
    plt.figure("Drunkard's Walks")
    plt.title(f"Drunkard's Walks. {k} steps. {n} walks.")
    plt.plot(sim[2], sim[3], linewidth=0.1)
    plt.plot(sim[0], sim[1], 'ro', markersize=5)
    plt.xlim(-1500, 1500)
    plt.ylim(-1500, 1500)
    all_distances[0].append(sim[0])
    all_distances[1].append(sim[1])
    x_paths.append(sim[2])
    y_paths.append(sim[3])
    
plt.show()

average_x = sum(all_distances[0]) / len(all_distances[0]) 
average_y = sum(all_distances[1]) / len(all_distances[1])

average_x_path = []
for i in range(len(x_paths)):
    average = 0
    sum = 0
    for path in x_paths:
        sum += path[i]
    average = sum / len(x_paths)    
    average_x_path.append(average)

average_y_path = []
for i in range(len(y_paths)):
    average = 0
    sum = 0
    for path in y_paths:
        sum += path[i]
    average = sum / len(y_paths)    
    average_y_path.append(average)

print(f'Average x for {n} walks with {k} steps is:', average_x)
print(f'Average y for {n} walks with {k} steps is:', average_y)


plt.figure("Average Drunkard's Walk")
plt.title(f"Average Drunkard's Walk. {k} steps. {n} walks.")
plt.plot(average_x_path, average_y_path)
plt.plot(average_x, average_y, 'ro', label=f'x={average_x}, y={average_y}', markersize=5)
plt.legend(loc='upper left')
plt.xlim(-1500, 1500)
plt.ylim(-1500, 1500)

plt.show()


x_points = all_distances[0]
y_points = all_distances[1]

plt.figure(f'x and y points for all {n} walks')
plt.title(f'x and y points for all {n} walks. Average x & y: {average_x}, {average_y}')
plt.scatter(x_points, y_points)
plt.plot(average_x, average_y, 'ro', markersize=5)

plt.show()
