from collections import deque

n, m = map(int, input().split())
grid = []
answer = 0

for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

queue = deque()
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(sx, sy):
    queue.append((sx, sy)) # start
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        if x == (n-1) and y == (m-1):
            return 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return 0
answer = bfs(0, 0)
print(answer)