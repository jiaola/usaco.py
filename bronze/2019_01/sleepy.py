import sys

sys.stdin = open('sleepy.in', 'r')
sys.stdout = open('sleepy.out', 'w')

n = int(input())
lst = [int(i) for i in input().split()]

n -= 1
while lst[n-1] < lst[n] and n > 0:
    n -= 1
print(n)