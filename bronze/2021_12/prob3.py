t = int(input())
for i in range(t):
    ans = 0
    n, k = map(int, input().split())
    grid = []
    for j in range(n):
        grid.append(input())
    # k == 1
    tr = 1
    bl = 1
    for j in range(n):
        if grid[0][i] == 'H' or g[i][n-1] == 'H':
            tr = 0
        if grid[i][0] == 'H' or g[n-1][i] == 'H':
            bl = 0
    ans += tr + bl 
    # k == 2
    if k >= 2:
        for j in range(1, n-1):
            valid = True
            for l in range(n):
                if grid[j][l] == 'H':
                    valid = False 
                if l < j and grid[0][l] == 'H':
                    valid = False 
                if l > j and grid[n-1][l] == 'H': 
                    valid = False 
                if not valid:
                    break
            if valid:
                ans += 1
        for j in range(n-1):
            valid = True 
            for l in range(n):
                if grid[l][j] == 'H':
                    valid = False 
                if l < j and grid[l][0] == 'H':
                    valid = False 
                if l > j and grid[l][n-1] == 'H':
                    valid = False 
                if not valid:
                    break 
            if valid:
                ans += 1
    # k == 3
    if k >= 3:
        ...
    print(ans)
     