def create_fiboLIST(x):
    if x == 0 :
        ls = [1]
    elif x == 1 :
        ls = [1, 1]
    else:
        ls = [1, 1]
        for i in range(1, x):
            fibo = ls[i] + ls[i-1]
            ls.append(fibo)
    return ls

def sum_fibo(ls, str):
    x = 0
    if str in ['E', 'e']:
        for i in range(len(ls)):
            if i % 2 == 0:
                x += ls[i]
    elif str in ['o', 'O']:
        for i in range(len(ls)):
            if i % 2 != 0:
                x += ls[i]
    return x    
#main
n = int(input())
command = str(input())
if n < 0:
    print('ERROR')
elif not(command in ['E', 'e', 'O', 'o']):
    print('ERROR')
elif n == 0 and command in ['o', 'O']:
    print("ERROR")
else:
    fibo_ls = create_fiboLIST(n)
    summy = sum_fibo(fibo_ls, command)
    print(summy)

        