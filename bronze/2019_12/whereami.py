import sys

sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

n = int(input())
s = input()

for i in range(n):
    ss = set()
    for j in range(n - i):
        ss.add(s[j:j + i + 1])
    if len(ss) == n - i:
        print(i + 1)
        break
