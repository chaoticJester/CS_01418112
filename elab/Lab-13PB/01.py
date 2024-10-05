def namelist(names):
    comma = len(names) - 2
    tmp = ''
    for name in names:
        tmp += name
        if comma > 0:
            tmp += ', '
        elif comma == 0:
            tmp += ' & '
        comma -= 1
    while ' ,' in tmp or ',  ' in tmp:
        tmp = tmp.replace(' ,', ',')
        tmp = tmp.replace(',  ', ', ')
    while '  &' in tmp or '&  ' in tmp:
        tmp = tmp.replace('  &', ' &')
        tmp = tmp.replace('&  ', '& ')
    return tmp

print( namelist(['Bart', 'Viola', 'Peter', 'Nostel', 'Bobby', 'James Violent']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )