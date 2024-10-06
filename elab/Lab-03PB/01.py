weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

BMI = weight / (height ** 2)

print(f"BMI is {BMI:.1f}")

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal weight")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
else:
    print("Obesity")