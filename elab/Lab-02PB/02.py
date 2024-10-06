width = float(input("Enter width: "))
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))

volumn = width * length * depth

total_t = (volumn * 15)/60

print(f"Time to fill a pool is {total_t:.2f} minutes.")