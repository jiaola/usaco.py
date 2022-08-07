def findMinDiff(lst):
    ans = 10 ** 8
    for i in range(len(lst)-1):
        ans = min(ans, abs(lst[i+1] - lst[i]))
    return ans

print(findMinDiff([23, 15, 46, 75, 6, 74, 100]))
print(findMinDiff([1, 34, 4,6, 14, 2]))