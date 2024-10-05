day = int(input())
hour = int(input())
minute = int(input())

if day == 2:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-monday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-monday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-monday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-monday.png")
elif day == 3:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-tuesday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-tuesday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-tuesday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-tuesday.png")
elif day == 4:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-wednesday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-wednesday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-wednesday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-wednesday.png")
elif day == 5:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-thursday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-thursday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-thursday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-thursday.png")
elif day == 6:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-friday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-friday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-friday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-friday.png")
elif day == 7:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-saturday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-saturday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-saturday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-saturday.png")
elif day == 1:
    if (4 <= hour < 12 and 0 < minute) or (hour == 12 and minute == 0):
        print("good-morning-sunday.png")   
    elif (12 <= hour < 18 and 0 < minute) or (hour == 18  and minute == 0):
        print("good-afternoon-sunday.png")
    elif (18 <= hour < 22 and 0 < minute) or (hour == 22 and minute == 0):
        print("good-evening-sunday.png")
    elif (22 <= hour < 24 and minute <= 1) or (0 <= hour <= 4 and minute <= 0):
        print("good-night-sunday.png")