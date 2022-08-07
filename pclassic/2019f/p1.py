def findPeak(lst):
    if lst[0] > lst[1]:
        return 0
    for i in range(1, len(lst)-1):
        if lst[i-1] < lst[i] and lst[i] > lst[i+1]:
            return i 
    return len(lst) - 1

print(findPeak([1, 2, 3]))
print(findPeak([13, 52, 75, -8, 27]))