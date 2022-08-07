n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * (n+1) # position of each item in b
for i in range(n):
    c[b[i]] = i

p = 0
cnt = 0
for i in range(n):
    if c[a[i]] >= p:
        cnt += 1
        p = c[a[i]] + 1

print(p - cnt)
