txt = str(input())

if txt == '':
    print('')
else:
    script = txt.split(' ')
    for i in range(len(script)):
        if not (script[i] in ['for', 'and', 'with', 'of']):
            script[i] = script[i][0].replace(script[i][0], script[i][0].upper()) + script[i][1:]
    print(' '.join(script))