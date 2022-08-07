import sys
 
sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')
 
def line_overlap(x1, x2, x3, x4):
    return max(0, min(x2, x4) - max(x1, x3))
 
def area_overlap(r1, r2):
    return line_overlap(r1[0], r1[2], r2[0], r2[2]) * line_overlap(r1[1], r1[3], r2[1], r2[3])
 
def area(r):
    return (r[2]-r[0]) * (r[3]-r[1])
 
r1 = [int(i) for i in input().split()]
r2 = [int(i) for i in input().split()]
r3 = [int(i) for i in input().split()]
 
print(area(r1) + area(r2) - area_overlap(r1, r3) - area_overlap(r2, r3))