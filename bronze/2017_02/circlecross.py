import sys

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

s, c, p = input(), {}, 0
for i in range(len(s)):
    if s[i] not in c:
        c[s[i]] = []
    c[s[i]].append(i)
c = list(c.values())
for i in range(26):
    for j in range(i + 1, 26):
        if c[i][0] < c[j][0] < c[i][1] < c[j][1] or c[j][0] < c[i][0] < c[j][1] < c[i][1]:
            p += 1
print(p)