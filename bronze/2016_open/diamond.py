import sys

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')

n, k = [int(i) for i in input().split()]
l = []
for i in range(n):
    l.append(int(input()))
l.sort()
m = 0
for i in range(n):
    t = 0
    for j in range(i+1, n):
        if l[j] - l[i] <= k:
            t += 1
    m = max(m, t+1)
print(m)
