dic = {}
origin_txt = str(input()).replace(' ','')
ls_txt = []
for ch in origin_txt:
    if not(ch in ls_txt):
        ls_txt.append(ch)
        
origin_code =str(input())
for i in range(len(origin_code)):
    dic.update({origin_code[i]:ls_txt[i]})

wanna_encrypt = [i for i in str(input())]
for i in range(len(wanna_encrypt)):
    if wanna_encrypt[i] in dic:
        wanna_encrypt[i] = dic.get(wanna_encrypt[i])

print(''.join(wanna_encrypt))
