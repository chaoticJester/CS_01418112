import math

x = float(input("Enter x : "))

if x < 0:
    f = math.sqrt(math.pow(x, 2) + 1)
elif x == 0:
    f = x
elif x > 0 and x <= 99:
    f = 3 * math.pow(x, 2) - math.pow(1-x, 2)
elif x > 99:
    f = 2 * (math.pow(x, 3)) - (x / math.sqrt((x+1)))

print(f"f({x:.2f}) = {math.ceil(f):.0f}")

