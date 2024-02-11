n, r, c = map(int, input().split())
route = []
visited = [[False] * n for _ in range(n)]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


def dfs(x, y):
    tx, ty = x, y
    temp = array[x][y]  # biggest value
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if array[nx][ny] > temp:
                tx, ty = nx, ny
                temp = array[nx][ny]
                break
    if tx == x and ty == y:
        return route
    else:
        route.append(temp)
        dfs(tx, ty)


route.append(array[r - 1][c - 1])
dfs(r - 1, c - 1)

print(*route)