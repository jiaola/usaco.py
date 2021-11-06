import sys

sys.stdin = open('traffic.in', 'r')
sys.stdout = open('traffic.out', 'w')

n = int(input())
rec = []
for _ in range(n):
    d, x, y = input().split()
    rec.append([d, int(x), int(y)])

lower, upper = -1000 * n, 1000 * n
for i in range(n-1, -1, -1):
    d, x, y = rec[i]
    if d == 'on':
        lower -= y
        upper -= x
        lower = max(0, lower)
    elif d == 'off':
        lower += x
        upper += y
    else:
        lower = max(lower, x)
        upper = min(upper, y)
print(lower, upper)

lower, upper = -1000*n, 1000 * n
for i in range(n):
    d, x, y = rec[i]
    if d == 'on':
        lower += x
        upper += y
    elif d == 'off':
        lower -= y
        upper -= x
        lower = max(0, lower)
    else:
        lower = max(lower, x)
        upper = min(upper, y)

print(lower, upper)