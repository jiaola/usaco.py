import sys

sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

n = int(input())
guards = []
for _ in range(n):
    guards.append([int(i) for i in input().split()])
ans = 0
for i in range(n):
    mx = 0
    for time in range(1001):
        covered = False
        for j in range(n):
            if j == i:
                continue
            if guards[j][0] < time <= guards[j][1]:
                covered = True
                break
        if covered:
            mx += 1
    ans = max(ans, mx)
print(ans)

