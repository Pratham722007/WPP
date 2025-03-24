import math

def edistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + 
                     (point1[1] - point2[1]) ** 2 + 
                     (point1[2] - point2[2]) ** 2)

def find_nearest_neighbors(points):
    nearestneighbors = []
    
    for i, point in enumerate(points):
        min_distance = float('inf')
        nearestneighbor = None
        
        for j, other_point in enumerate(points):
            if i != j:
                distance = edistance(point, other_point)
                if distance < min_distance:
                    min_distance = distance
                    nearestneighbor = other_point
        
        nearestneighbors.append((point, nearestneighbor))
    
    return nearestneighbors


points = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15),
    (16, 17, 18),
    (19, 20, 21),
    (22, 23, 24),
    (25, 26, 27),
    (28, 29, 30)
]

nearestneighbors = find_nearest_neighbors(points)

for pair in nearestneighbors:
    print(f"Point: {pair[0]}, Nearest Neighbor: {pair[1]}")
