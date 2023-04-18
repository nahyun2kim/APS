def dot_star(idx):
    if idx == 1:
        return ['*']
    t = dot_star(idx - 1)
    stars = ['*' * (len(t) + 4), '*' + ' ' * (len(t) + 2) + '*']
    for t in t:
        new_t = '* ' + t + ' *'
        stars.append(new_t)
    stars.append('*' + ' '*(len(t)+2) + '*')
    stars.append(stars[0])
    return stars


n = int(input())
star = dot_star(n)

for s in star:
    print(s)