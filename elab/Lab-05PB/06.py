n = int(input())
sumn = 0

while True:
    if n <= 0:
        break
    sumn += n % 10
    n = n // 10

    
if sumn % 9 == 0:
    print(f"Yes {sumn}")
else : 
    print(f"No {sumn % 9}")