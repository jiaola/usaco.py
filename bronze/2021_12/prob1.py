n = int(input())
s = input()
ans = 0
for i in range(n):
    left = 0
    if i > 0 and s[i-1] != s[i]:
        left = 1
        k = i - 2
        while k >= 0 and s[k] == s[i-1]:
            left += 1
            k -= 1
    right = 0
    if i < n-1 and s[i+1] != s[i]:
        right = 1
        k = i + 2
        while k < n and s[k] == s[i+1]:
            right += 1
            k += 1
    ans += left * right
    if left > 1:
        ans += left - 1
    if right > 1:
        ans += right - 1
print(ans)