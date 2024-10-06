def bigram(txt):
    ls = []
    for i in range(len(txt)-1):
        tmp = txt[i].lower() + txt[i+1].lower()
        if not(tmp in ls):
            ls.append(tmp)
    return ls
txt = str(input())
split_txt = bigram(txt)
split_txt.sort() 
for bi in split_txt:
    print(bi)