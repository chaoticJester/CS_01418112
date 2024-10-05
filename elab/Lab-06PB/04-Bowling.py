frame = 1
point = 0

while frame <= 10:
    print(f"Frame # {frame}")
    pin = int(input("  Number of pins down: "))

    if pin == 10:
        point += 10
        frame += 1
        continue
    else:
        if 10 - pin != 0:
            print(f"Frame # {frame}")
            S_pin = int(input(f"  Number of pins down (0-{10-pin}): "))
            if (10 - pin) - S_pin != 0 :
                point += pin + S_pin
                frame += 1 
                continue
            elif (10 - pin) - S_pin == 0:
                point += 10
                frame += 1
                continue

print(f"Total score is {point}")