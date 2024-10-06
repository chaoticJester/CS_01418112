# input
inc = float(input())
ex = float(input())

# output
print("1234567890" * 3)
print("{:<13}".format("Total Income") + f"{inc:>+8.2f}" + " bahts")
print("{:<13}".format("Expense") + f"{ex:>8.2f}" + " bahts")
print("{:<13}".format("Profit") + f"{inc+ex:0>8.2f}" + " bahts")