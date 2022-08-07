n = int(input())
p = [int(i) for i in input().split()]
t = [int(i) for i in input().split()]
d = [p[i]-t[i] for i in range(n)]
prev = 0
ans = 0
for i in range(n):
    if d[i] > prev:
        ans += d[i] - prev 
    prev = d[i]
if prev < 0:
    ans += -prev
print(ans)
