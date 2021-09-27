import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

n, m = map(int, input().split())
spotty = []
plain = []

for _ in range(n):
	spotty.append(input())
for _ in range(n):
	plain.append(input())

ans = 0
for i in range(m):
	s1 = set()
	s2 = set()
	for genome in spotty:
		s1.add(genome[i])
	for genome in plain:
		s2.add(genome[i])
	if s1.isdisjoint(s2):
		ans += 1
print(ans)
