def wrong_month(ls):
    for month in ls:
        if int(month[3::]) < 1 or int(month[3::]) > 12:
            return True
    return False

def wrong_day(ls):
    for day in ls:
        if int(day[3::]) in [1,3,5,7,8,10,12] and (int(day[0:2]) < 1 or int(day[0:2]) > 31):
            return True
        elif int(day[3::]) in [4,6,9,11] and (int(day[0:2]) < 1 or int(day[0:2]) > 30):
            return True
        elif int(day[3::]) == 2 and (int(day[0:2]) < 1 or int(day[0:2]) > 28):
            return True
    return False

def sort_daynmonth(ls):
    tmp_ls = ls
    tmp = ''
    for data in tmp_ls:
        if tmp == '':
            tmp = data
            continue
        else:
            if int(tmp[3:]) < int(data[3:]):
                break
            elif int(tmp[3:]) > int(data[3:]):
                tmp2 = data
                tmp_ls[1] = tmp
                tmp_ls[0] = tmp2
            elif int(tmp[3:]) == int(data[3:]):
                if int(tmp[:2]) < int(data[:2]):
                    break
                elif int(tmp[:2]) > int(data[:2]):
                    tmp2 = data
                    tmp_ls[1] = tmp
                    tmp_ls[0] = tmp2
                elif int(tmp[:2]) == int(data[:2]):
                    break
    return tmp_ls

def convert_to_day(str):
    day = 0
    month = int(str[3:])
    for m in range(month):
        if m in [1,3,5,7,8,10,12]:
            day += 31
        elif m in [4,6,9,11]:
            day += 30
        elif m == 2:
            day += 28
    day += int(str[:2])
    return day

def count_sunday(x, y, z):
    sunday = 0
    fs = z
    for i in range(y+1):
        if fs >= x and fs <= y:
            sunday += 1
        fs += 7
    return sunday
        
#main
boundary = []
for i in range(2):
    date = str(input())
    boundary.append(date)
first_sund = int(input())

if wrong_month(boundary):
    print("Wrong Month")
if wrong_day(boundary):
    print("Wrong Day")
if not(wrong_month(boundary)) and not(wrong_day(boundary) and 0 < first_sund < 8):
    sorted_bound = sort_daynmonth(boundary)
    b1 = convert_to_day(sorted_bound[0])
    b2 = convert_to_day(sorted_bound[1])
    total_sunday = count_sunday(b1, b2, first_sund)
    print(total_sunday)