import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, input().split())
c, d = map(int, input().split())
ans = 0
for i in range(0, 101):
    if a <= i < b or c <= i < d:
        ans += 1
print(ans)
