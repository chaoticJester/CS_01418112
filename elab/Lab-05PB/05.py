num = int(input("Enter height: "))
s1 = (num-1) * 2
count = 0
s2 = 0

while count < num:
    if count == 0:
        print(" "*s1 + "1")
    elif count == 1:
        s2 += 3
        print(" " * s1 + "1" + " " * s2 + "1")
    else:
        s2 +=4
        print(" " * s1 + "1" + " " * s2 + "1")
    count += 1
    s1 -= 2