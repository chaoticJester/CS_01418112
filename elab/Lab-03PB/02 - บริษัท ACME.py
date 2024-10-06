buy_amount = float(input("Enter buying amount: "))

if buy_amount >= 3000:
    af_dis = buy_amount - (buy_amount * 0.15)
elif buy_amount >= 1000 and buy_amount < 3000:
    af_dis = buy_amount - (buy_amount * 0.10)
elif buy_amount < 1000:
    af_dis = buy_amount - (buy_amount * 0)
    
print(f"Amount due after discount is {af_dis:.2f} baht.")
