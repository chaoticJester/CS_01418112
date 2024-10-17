def digit(n):
    one = n % 10
    return one

def tens(n):
    ten = n % 100
    ten = ten // 10
    return ten

def hundreds(n):
    hun = n % 1000
    hun = hun // 100
    return hun

def thousands(n):
    thou = n // 1000
    return thou

def sum_digits(n):
    sum = digit(n) + tens(n) + hundreds(n) + thousands(n)
    return sum

n   = int(input('Enter a number (0 to 9999): '))
print(f'Digit place is {digit(n)}.')
print(f'Tens place is {tens(n)}.')
print(f'Hundreds place is {hundreds(n)}.')
print(f'Thousands place is {thousands(n)}.')
print(f'Sum of all digits is {sum_digits(n)}.')