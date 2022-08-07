
def solve():
    word = input()
    for c in word:
        if c not in letters:
            return "NO"

    if len(word) == 2:
        for i in letters[word[0]]:
            for j in letters[word[1]]:
                if i != j:
                    return "YES"
        return "NO"

    if len(word) == 3:
        for i in letters[word[0]]:
            for j in letters[word[1]]:
                for k in letters[word[2]]:
                    if i != j and i != k and j != k:
                        return "YES"
        return "NO"

    if len(word) == 4:
        for i in letters[word[0]]:
            for j in letters[word[1]]:
                for k in letters[word[2]]:
                    for l in letters[word[3]]:
                        if len(set([i, j, k, l])) == 4:
                            return "YES"
        return "NO"
    
    return "NO"

n = int(input())
letters = {}
for i in range(4):
    s = input()
    for c in s:
        if c not in letters:
            letters[c] = set()
        letters[c].add(i)
# print(letters)

for _ in range(n):
    print(solve())
