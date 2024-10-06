def find_close_v(ls):
    m = 1000000000000000000000000000000000000000000000000
    for i in range(len(ls)):
        if i == len(ls)-1:
            break
        if abs(ls[i] - ls[i+1]) < m:
            m = abs(ls[i] - ls[i+1])
    return m

def find_closest_n(x, ls):
    c_ls = []
    for i in range(len(ls)):
        if i == len(ls)-1:
            break
        if abs(ls[i] - ls[i+1]) == x:
            c_ls.append(f"{ls[i]} {ls[i+1]}")
    return c_ls
#main
n = int(input())
n_ls = []
for i in range(n):
    num = int(input())
    n_ls.append(num)
n_ls.sort()

close = find_close_v(n_ls)
ls_closest = find_closest_n(close, n_ls)
print("\n".join(ls_closest))