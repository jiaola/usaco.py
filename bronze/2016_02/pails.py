import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

x, y, m = map(int, input().split())
mx = 0
for i in range(0, m // x + 1):
    for j in range(0, m // y + 1):
        z = i * x + j * y
        if z <= m:
            mx = max(mx, z)
        else:
            break
print(mx)
