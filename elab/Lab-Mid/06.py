num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 > num2 > num3) and ((num3**2) + (num2**2) == num1**2):
    print("True")
elif (num1 > num3 > num2) and ((num2**2) + (num3**2) == num1**2):
    print("True")
elif (num2 > num1 > num3) and ((num3**2) + (num1**2) == num2**2):
    print("True")
elif (num2 > num3 > num1) and ((num1**2) + (num3**2) == num2**2):
    print("True")
elif (num3 > num1 > num2) and ((num2**2) + (num1**2) == num3**2):
    print("True")
elif (num3 > num2 > num1) and ((num1**2) + (num2**2) == num3**2):
    print("True")
else :
    print("False")