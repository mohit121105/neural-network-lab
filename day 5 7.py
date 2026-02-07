import math


points = [
    ((2, 3), 'A'),
    ((5, 4), 'B'),
    ((2, 4), 'A')
]


x = int(input("Enter x: "))
y = int(input("Enter y: "))
new_point = (x, y)

nearest_class = None
min_distance = float('inf')

4
for (px, py), label in points:
    distance = math.sqrt((x - px)**2 + (y - py)**2)
    
    if distance < min_distance:
        min_distance = distance
        nearest_class = label

print("Nearest class is:", nearest_class)
