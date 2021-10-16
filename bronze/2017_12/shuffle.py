import sys

sys.stdin = open('shuffle.in', 'r')
sys.stdout = open('shuffle.out', 'w')

n = int(input())
a = [int(i) for i in input().split()]
cows = input().split()

for i in range(3):
    shuffled = []
    for j in range(n):
        shuffled.append(cows[a[j]-1])
    cows = shuffled
print('\n'.join(cows))
