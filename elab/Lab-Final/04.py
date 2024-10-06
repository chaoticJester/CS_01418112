txt = str(input())
c = 0
for i in range(len(txt)):
    if txt[i] in [',', ' ', '.']:
        continue
    if i == 0:
        tmp = txt[i]
        c += 1
    if ord(tmp.lower()) < ord(txt[i].lower()):
        tmp = txt[i]
        c += 1
    elif ord(tmp.lower()) > ord(txt[i].lower()):
        break
print(c)
