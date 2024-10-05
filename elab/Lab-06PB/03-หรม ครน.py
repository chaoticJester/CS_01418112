f_num = int(input("Enter the first number: "))
s_num = int(input("Enter the second number: "))

num1 = f_num
num2 = s_num



while True:

    remainder = num1 % num2

    if remainder == 0:
        break

    num1 = num2
    num2 = remainder

print(f"  >> gcd({f_num}, {s_num}) ={num2:>7}")
print(f"  >> lcm({f_num}, {s_num}) ={f_num * s_num / num2:>7.0f}")





    