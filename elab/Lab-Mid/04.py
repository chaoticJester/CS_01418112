while True:
    print("<<Point a>>")
    x_a = int(input("Enter x coordinate: "))
    y_a = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    x_b = int(input("Enter x coordinate: "))
    y_b = int(input("Enter y coordinate: "))
    
    if x_a == 0 or x_b == 0 or y_a == 0 or y_b == 0:
        print("Goodbye")
        break

    euclidean = ((x_a - x_b)**2 + (y_a - y_b)**2)**0.5

    if x_a == x_b and y_a == y_b:
        horizontal = 0
        vertical = 0
    else:
        horizontal = abs(x_a - x_b)
        vertical = abs(y_a - y_b)

    print(f"Distance between ({x_a}, {y_a}) and ({x_b}, {y_b}):")
    print(f"Euclidean distance is {euclidean:.2f}.")
    print(f"Horizontal distance is {horizontal}.")
    print(f"Vertical distance is {vertical}.")

    if x_a == x_b and y_a < y_b:
        print("We are going north.")
    elif x_a == x_b and y_a > y_b:
        print("We are going south.")
    elif x_a < x_b and y_a == y_b:
        print("We are going east.")
    elif x_a > x_b and y_a == y_b:
        print("We are going west.")
    elif x_a > x_b and y_a > y_b:
        print("We are going south-west.")
    elif x_a < x_b and y_a > y_b:
        print("We are going south-east.")
    elif x_a < x_b and y_a < y_b:
        print("We are going north-east.")
    elif x_a > x_b and y_a < y_b:
        print("We are going north-west.")
    elif x_a == x_b and y_a == y_b:
        print("We are going nowhere.")