txt = str(input())
command = int(input())
if command == 0 or txt == '':
    print(txt)
else :
    shift = command % len(txt)
    res = txt[-shift:] + txt[:-shift]
    print(str(res))
