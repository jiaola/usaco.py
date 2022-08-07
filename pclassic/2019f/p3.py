def floodfill(x, y, m):
    nrow = len(m)
    ncol = len(m[0])
    if x < 0 or y < 0 or x >= len(m) or y >= len(m[0]) or m[x][y] == 0:
        return m
    m[x][y] = 0
    m = floodfill(x-1, y, m)
    m = floodfill(x+1, y, m)
    m = floodfill(x, y-1, m)
    m = floodfill(x, y+1, m)
    return m

def bitSpill(x, y, m):
    m = floodfill(x, y, m)
    return m 

m = [[1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1]]

m = bitSpill(2, 1, m)
for i in range(len(m)):
    print(' '.join([str(c) for c in m[i]]))
