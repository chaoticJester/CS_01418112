txt = str(input())
weaved = ''
n = len(txt)-1
for i in range(len(txt)//2):
    weaved += txt[i] + txt[n]
    n -= 1
if len(txt) % 2 != 0:
    weaved += txt[len(txt)//2]
print(weaved)
