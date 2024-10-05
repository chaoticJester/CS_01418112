saw = 0
f_height = 0
check_height = 0

while True:
    height = int(input())

    if height == -1:
        break

    if saw == 0:
        saw += 1
        f_height = height
        continue
    else:
        if saw == 1 and f_height > height:
            check_height = height
            continue
        elif saw == 1 and f_height == height:
            check_height = height
            continue
        elif check_height < height:
            check_height = height
            saw += 1
        elif check_height == height:
            check_height = height
            continue

print(saw)
            
    
    
        
    
