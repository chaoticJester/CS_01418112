def decrease(ls):
    ls_copy = ls
    for i in range(len(ls_copy)-1):
        if ls_copy[i] >= ls_copy[i+1]:
            continue
        else:
            return False
    return True

def increase(ls):
    ls_copy = ls
    count = 0
    tmp = None
    for i in range(len(ls_copy)-1):
        if ls_copy[i] <= ls_copy[i+1]:
            continue
        else:
            return False
    return True

def rando(ls):
    ls_copy = ls 
    inc = 0
    dec = 0
    for i in range(len(ls_copy)-1):
        if ls_copy[i] > ls_copy[i+1]:
            dec += 1
        if ls_copy[i] < ls_copy[i+1]:
            inc += 1
    if inc and dec:
        return True
    else:
        return False

#main
ls_n = []
while True:
    num = int(input("Enter a number (-1 to end): "))
    if num == -1:
        break
    if num < 0 or num > 100 :
        print("Number is out of range.")
        continue    
    ls_n.append(num)
    
print("-----")
print("Original list:")
print(ls_n)

if len(ls_n) == 0:
    print("The list is empty.")
elif rando(ls_n):
    print("The list is in random order.")
elif increase(ls_n) == False and decrease(ls_n) == True:
    print("The list is in non-increasing order.")
elif increase(ls_n) == True and decrease(ls_n) == False:
    print("The list is in non-decreasing order.")
else:
    print("The list is in non-increasing and non-decreasing order.")