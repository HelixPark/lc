# -*- coding:utf-8 -*-
# import sys
# line = sys.stdin.readline().strip()
# values = list(map(int, line.split(',')))
# m, n = values[0], values[1]
# data = []
#
# for _ in range(m):
#     line = sys.stdin.readline().strip()
#     row = []
#     for i in range(n):
#         row.append(line[i])
#     data.append(row)
data = [['s','s','h','h','h'],
        ['s','s','h','h','h'],
        ['h','h','s','h','h'],
        ['h','h','h','s','s'],]

def dfs(grid, r, c):
    grid[r][c] = 'h'
    nr, nc = len(grid), len(grid[0])
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "s":
            dfs(grid, x, y)

def numIslands(grid):
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])

    num_islands = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == "s":
                dfs(grid, r, c)

                num_islands += 1

    return num_islands
print(numIslands(data))