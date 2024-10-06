print("Upper left corner coordinate: ")

x = int(input("  << x axis: "))
y = int(input("  << y axis: "))
east = int(input("  << Eastern: "))
south = int(input("  << Southern: "))

print("Enter a coordinate: ")

check_x = int(input("  << x axis: "))
check_y = int(input("  << y axis: "))

if (x <= check_x <= (x + east)) and ((y - south) <= check_y <= y):
        print(f">>> ({check_x:.2f}, {check_y:.2f}) is inside the rectangle.")
else : 
    print(f">>> ({check_x:.2f}, {check_y:.2f}) is not inside the rectangle.")
