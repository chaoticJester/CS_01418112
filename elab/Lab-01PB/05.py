block_length = 12
block_width = 9
house_length = 7
house_width = 6
MOW_RATE = 35.0
#----------------------------------------------------------------
area = (block_length*block_width) - (house_length*house_width)
price = area * MOW_RATE
print("Mowing cost is", price, "baht.")