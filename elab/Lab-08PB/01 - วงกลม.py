import math
def circle(r):
    area = math.pi * math.pow(r, 2)
    return area

def circumference(r):
    cirCUM = 2 * math.pi * r
    return cirCUM

def sphere(r):
    v = (4/3) * math.pi * math.pow(r, 3)
    return v

r = float(input("Enter a radius: "))
print('Area of a circle with radius {:.2f} is {:.2f}.'.format(r, circle(r)))
print('Circumference of a circle with radius {:.2f} is {:.2f}.'.format(r, circumference(r)))
print('Volume of sphere with radius {:.2f} is {:.2f}.'.format(r, sphere(r)))