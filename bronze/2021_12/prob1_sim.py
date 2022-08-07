n = int(input())
s = list(input())
ans = 0
for i in range(3, n+1):
    j = 0
    n_g = 0
    n_h = 0
    for k in range(0, i):
        if s[k] == 'G':
            n_g += 1
        else:
            n_h += 1 
    if n_h == 1 or n_g == 1:
        ans += 1
    while j + i < n:
        if s[j] == 'G':
            n_g -= 1
        else:
            n_h -= 1
        if s[j+i] == 'G':
            n_g += 1
        else:
            n_h += 1
        if n_g == 1 or n_h == 1:
            ans += 1
        j += 1
print(ans)

