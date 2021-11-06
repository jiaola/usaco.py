import sys

sys.stdin = open('guess.in', 'r')
sys.stdout = open('guess.out', 'w')

n = int(input())
tot = []
for i in range(n):
    tot.append([i for i in input().split()][2:])
cm = []
for i in range(len(tot)):
    tot2 = tot.copy()
    tot2.remove(tot[i])
    for j in range(len(tot2)):
        l = set()
        k = set()
        for z in tot2[j]:
            l.add(z)
        for f in tot[i]:
            k.add(f)
        lk = l & k
        cm.append(len(lk)+1)
print(max(cm))