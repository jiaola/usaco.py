import sys

sys.stdin = open('times17.in', 'r')
sys.stdout = open('times17.out', 'w')

n = input()
x = int(n, 2)
print(f'{x * 17:b}')
# print(bin(x*17)[2:])
