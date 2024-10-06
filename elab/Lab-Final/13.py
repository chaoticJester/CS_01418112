number = {
    '1' : "one",
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',
    '90' : 'ninety'
} 
    
txt = str(input())

if len(txt) > 3 or not(txt.isdigit()) or txt == '':
    print("ERROR")
else:
    if len(txt) == 3:
        num_txt = number.get(txt[0]) + '-hundred'
        if txt[1] == '1':
            num_txt += '-' + number.get(txt[1:])
        elif txt[1:] == '00':
            pass
        elif txt[1] == '0':
            num_txt += '-' + number.get(txt[2])
        elif txt[2] == '0' and txt[1] != '0':
            num_txt += '-' + number.get(txt[1]+'0')
        else:
            num_txt += '-' + number.get(txt[1]+"0") + '-' + number.get(txt[2])
    elif len(txt) == 2:
        if txt[0] == '1' or txt[1] == '0':
            num_txt = number.get(txt[0:])
        else:
            num_txt = number.get(txt[0]+'0') + '-' + number.get(txt[1])
    else:
        num_txt = number.get(txt)
    print(num_txt)