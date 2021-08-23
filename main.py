import math  # Built in math module for the sqrt function


def octahedron_area_and_volume(edge_length):
    area = 2 * (math.sqrt(3)) * (edge_length * edge_length)  # Octahedron area formula
    print('\nHere\'s the area')
    print(area)  # Printing the Octahedron area
    print('Here\'s the volume')
    volume = ((edge_length * edge_length * edge_length) * (math.sqrt(2) / 3))  # Octahedron volume formula
    print(f'{volume}')  # Printing the Octahedron volume


octahedron_area_and_volume(int(input('Please enter the edge length\n')))
