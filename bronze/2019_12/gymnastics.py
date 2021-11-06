import sys

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = [int(i) for i in input().split()]
pairs = []
for i in range(n):
    pairs.append([0] * n)

r = []
for i in range(k):
    r.append([int(i) for i in input().split()])

cp = []
for i in range(n):
    for j in range(i+1, n):
        i_before_j = set()
        for k in r:
            i_before_j.add((k.index(i+1) < k.index(j+1)))
        if len(i_before_j) == 1:
            cp.append((i, j))
print(len(cp))
