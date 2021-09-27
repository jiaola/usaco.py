import sys

sys.stdin = open("pails.in", "r")
sys.stdout = open("pails.out", "w")

a, b, c = map(int, input().split())
mx = 0
for i in range(0, c // a + 1):
    for j in range(0, c // b + 1):
        m = i * a + j * b
        if m <= c:
            mx = max(mx, m)
        else:
            break
print(mx)