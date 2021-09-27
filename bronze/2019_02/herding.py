import sys

sys.stdin = open('herding.in', 'r')
sys.stdout = open('herding.out', 'w')

p = [int(i) for i in input().split()]
p.sort()
d1 = p[1] - p[0]
d2 = p[2] - p[1]

if d1 == d2 == 1:
    print(0)
elif d1 == 2 or d2 == 2:
    print(1)
else:
    print(2)
print(max(d1, d2) - 1)


