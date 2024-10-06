import math

r = int(input("Enter a radius: "))

a_c = math.pi*r*r
cir = 2*math.pi*r

print(f"Area of a circle with radius {r} is {a_c:.2f}")
print(f"Circumference of a circle with radius {r} is {cir:.2f}")