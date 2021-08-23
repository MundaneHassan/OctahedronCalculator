import math  # Built in math module for the sqrt function
a = int(input('Please enter the edge length'))  # Taking the edge length of the regular octahedron
area = 2 * (math.sqrt(3)) * (a * a)  # Octahedron area
volume = ((a * a * a) * (math.sqrt(2)/3))  # Octahedron volume
print('Here\'s the area')
print(str(round(area, 2)))  # Printing the area
print('\nHere\'s the volume')
print(str(round(volume, 2)))  # Printing the volume
