def factors(n):
    f = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            f.add(i)
            f.add(n//i)
    return f

def check(lst, n, p):
    s = 0
    for i in range(n):
        s += lst[i]
        if s == p:
            s = 0
        elif s > p:
            return False
    return s == 0


def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    if len(set(lst)) == 1:
        return 0
    s = sum(lst)
    mx = max(lst)
    f = list(factors(s))
    f.sort()
    for i in f:
        if i < mx:
            continue
        if check(lst, n, i):
            return n - s // i
    return n - 1
    
t = int(input())
for  _ in range(t):
    print(solve())