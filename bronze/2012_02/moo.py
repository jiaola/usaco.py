import sys

sys.stdin = open('moo.in', 'r')
sys.stdout = open('moo.out', 'w')


def length(k):
    if k == -1:
        return 0
    else:
        return length(k-1) * 2 + k + 3


def solve(n, k):
    if n > length(k):
        return solve(n, k+1)
    if n < length(k-1):
        return solve(n, k-1)
    n -= length(k-1)
    if n < k+3:
        if n == 1:
            return 'm'
        else:
            return 'o'
    n -= k+3
    return solve(n, k-1)


n = int(input())
print(solve(n, 0))