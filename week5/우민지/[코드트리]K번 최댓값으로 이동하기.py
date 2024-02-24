from collections import deque

n, k = map(int, input().split())

grid = []

for i in range(n):
    grid.append(list(map(int, input().split())))

r, c = map(int, input().split())  # 시작 위치

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]


def bfs(sx, sy):
    # print(sx, sy)
    # print("now value :", grid[sx][sy])
    ex, ey = sx, sy
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((sx, sy))
    start_num = grid[sx][sy]  # 시작 위치 숫자
    visited[sx][sy] = True
    max_value = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (not visited[nx][ny]) and grid[nx][ny] < start_num:
                new_num = grid[nx][ny]
                visited[nx][ny] = True

                if new_num > max_value:
                    ex, ey = nx, ny
                    max_value = new_num
                elif new_num == max_value:
                    if nx < ex:  # 행 번호가 작은 곳으로 이동하기
                        ex, ey = nx, ny
                    elif nx == ex:
                        if ny < ey:
                            ex, ey = nx, ny

                queue.append((nx, ny))

    return ex, ey


r, c = r - 1, c - 1

for _ in range(k):
    nr, nc = bfs(r, c)  # 새로운 위치로 갱신
    if r == nr and c == nc:
        break
    else:
        r, c = nr, nc

# k 번 반복 후 갱신된 위치
print(r + 1, c + 1)