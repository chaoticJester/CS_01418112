def mother(str):
    for ch in str:
        if ch in ['a','e','i','o','u']:
            tmp = str[str.find(ch)+1:]
            return tmp
    return str

def father(str):
    count = 0 
    vowel = 0
    for ch in str:
        if ch in ['a','e','i','o','u']:
            vowel += 1
        if vowel == 2:
            break
        count += 1
    if vowel == 2:
        tmp = str[:count]
        return tmp
    else:
        return str
front = str(input())
end = str(input())
mix_name = father(front) + mother(end)
print(mix_name)