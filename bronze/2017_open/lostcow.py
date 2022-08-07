import sys

sys.stdin = open('lostcow.in', 'r')
sys.stdout = open('lostcow.out', 'w')

x, y = [int(i) for i in input().split()]
n = 0  # number of turns
d = 1  # direction
ans = 0 
p = x  # position
while not (x < y <= p  or p <= y < x):        
    p_new = x + (2 ** n) * d
    ans += abs(p_new - p)
    n += 1
    d = -d
    p = p_new
ans -= abs(p - y) 
print(ans)
