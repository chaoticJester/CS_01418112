m_scale = str(input()).split(',')
m_scale.pop(-1)
n = int(input())
count = 0 
while n > 0:
    if count == len(m_scale):
        count = 0
    n -= 1
    count += 1
print(m_scale[count-1])