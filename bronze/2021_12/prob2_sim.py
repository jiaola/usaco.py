n = int(input())
p = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
d = [p[i]-t[i] for i in range(n)]

first = 0
ans = 0
while True:
    while first < n and d[first] == 0:
        first += 1
    if first == n:  # all zeros
        break
    last = first 
    while last < n-1 and d[last] * d[last+1] > 0: # same sign as the next
        last += 1
    for i in range(first, last+1):
        if d[i] > 0:
            d[i] -= 1
        else:
            d[i] += 1
    ans += 1
print(ans)
    
