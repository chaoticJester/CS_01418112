txt = str(input())
n = len(txt) - 1
if len(txt) == 1:
    print(txt)
else:
    if len(txt) % 2 == 0:
        script = txt[n // 2::-1] + txt[-1:n // 2 :-1]
    else:
        script = txt[n // 2 - 1::-1] + txt[n // 2] + txt[-1:n // 2 :-1]
    print(script)