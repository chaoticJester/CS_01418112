level = int(input("Enter level pokemon: "))
balls = str(input("Enter level pokeball: "))
distance = int(input("Enter distance: "))

if balls in "Hh":
    b_qual = 0.01
elif balls in "Mm":
    if level >= 0 and level < 41 :
        b_qual = 0.03
    elif level >=41 and level < 61 :
        b_qual = 0.05
    elif 61 <= level and level < 101 :
        b_qual = 0.08
elif balls in "Ll":
    if level >= 0 and level < 41 :
        b_qual = 0.05
    elif level >=41 and level < 61 :
        b_qual = 0.03
    elif 61 <= level and level < 101 :
        b_qual = 0.1
         
suc_rate = 100 - (level * distance * b_qual)

if suc_rate > 100:
    suc_rate = 100.00
elif suc_rate < 0:
    suc_rate = 0.00

print(f"{suc_rate:.2f} percent.")
