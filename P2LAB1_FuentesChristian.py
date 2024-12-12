# Christian Fuentes
# 11/21/2024
# P2LAB1
# This Program calculates the area of a circle
import math
radius = float(input('What is the radius of the circle? '))
diam = radius*2
circ = 2*math.pi*radius
area = math.pi*radius**2
print(f'{"The diameter of the circle is"}, {diam:.1f}')
print(f'{"The circumfrence of the circle is"}, {circ:.2f}')
input()
