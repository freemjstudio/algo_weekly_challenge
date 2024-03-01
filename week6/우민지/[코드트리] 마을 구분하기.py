from collections import deque

n = int(input())
grid = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    grid.append(list(map(int, input().split())))

answer = 0 # 마을 개수
count_list = []
# 상 하 좌 우 움직이기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    count = 1
    visited[i][j] = True
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return count

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            count = bfs(i, j)
            count_list.append(count)
            answer += 1 # 마을의 개수 카운트

#### ANSWER ####
count_list.sort()
print(answer)
for c in count_list:
    print(c)