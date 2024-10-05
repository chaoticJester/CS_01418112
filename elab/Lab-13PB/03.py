total_type = int(input())
money_denominator = []
for i in range(total_type):
    deno = int(input())
    money_denominator.append(deno)
money_denominator.sort(reverse=True)
Money = int(input())

for type in money_denominator:
    temp = Money // type
    Money -= temp * type
    print(f"{type}: {temp}")
