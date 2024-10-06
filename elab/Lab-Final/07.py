damage_p_ammo = int(input())
zomby_hp = [int(i) for i in str(input()).split()]

ammo_count = []
ammo_used = 0
for zombie in zomby_hp:
    count = 0
    while zombie > 0:
        zombie -= damage_p_ammo
        count += 1
    ammo_used += count
    ammo_count.append(str(ammo_used))

print(ammo_used)
print(' '.join(ammo_count))