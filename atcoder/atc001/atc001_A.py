import sys
sys.setrecursionlimit(500*500)

H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

def dfs(x, y):
  if (0 <= x <= H-1) and (0 <= y <= W-1):
    if c[x][y] != '#':
      c[x][y] = '#'
      dfs(x+1, y)
      dfs(x, y+1)
      dfs(x-1, y)
      dfs(x, y-1)

def route(c):
  H, W = len(c), len(c[0])
  for i in range(H):
    for j in range(W):
      if c[i][j] == 's':
        sx, sy = i, j
      elif c[i][j] == 'g':
        gx, gy = i, j

  dfs(sx, sy)
  if c[gx][gy] == '#':
    print('Yes')
    return
  else:
    print('No')
    return

route(c)