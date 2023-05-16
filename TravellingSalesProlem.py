#Nurul Aliyah Dyah Sakhinah - F55121069

import itertools

def tsp(cities):
    shortest_path = None
    shortest_distance = float('inf')
    for path in itertools.permutations(cities):
        distance = 0
        for i in range(len(path) - 1):
            distance += dist(path[i], path[i+1])
        distance += dist(path[-1], path[0])
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path
    return shortest_path, shortest_distance

def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

# Example usage
cities = [(0, 0), (1, 2), (3, 1), (2, 3)]
shortest_path, shortest_distance = tsp(cities)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
