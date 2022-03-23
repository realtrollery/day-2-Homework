from collections import deque


def BFS(x, y):
  q.append([x, y])
  grid[y][x] = "1"
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  while q:
      t = q.popleft()
      tx = t[0]
      ty = t[1]
      for i3 in range(4):
          tempX = tx + dx[i3]
          tempY = ty + dy[i3]
          if 0 <= tempX < N and 0 <= tempY < M:
              if grid[tempY][tempX] == "0":
                  q.append([tempX, tempY])
                  grid[tempY][tempX] = "1"


q = deque()
N, M  = map(int, input().split())
chunk = 0
grid = []
for i in range(M):
    grid.append(list(input()))
for y1 in range(M):
    for x1 in range(N):
        if grid[y1][x1] == "0":
            BFS(x1, y1)
            chunk += 1
print(chunk)
