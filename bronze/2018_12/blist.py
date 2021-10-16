import sys

sys.stdin = open('blist.in', 'r')
sys.stdout = open('blist.out', 'w')

n = int(input())
bucket_list = []
for _ in range(n):
    start, end, bucket = map(int, input().split())
    bucket_list.append((start, bucket))
    bucket_list.append((end, -bucket))
bucket_list.sort()
total = 0
available = 0
for item in bucket_list:
    time, bucket = item
    if bucket > 0:
        if bucket > available:
            total += bucket - available
            available = 0
        else:
            available -= bucket
    else:
        available -= bucket
print(total)
