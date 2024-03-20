n = int(input())
grid = []
INF = int(1e9)
answer = INF
sx, sy = 0, 0  # start
ex, ey = n - 1, n - 1  # end

for i in range(n):
    line = list(input())
    for j in range(n):
        if line[j] == 'S':
            sx, sy = i, j
        if line[j] == 'E':
            ex, ey = i, j

    grid.append(line)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(n)]


def is_in_range(x, y):
    if (0 <= x < n) and (0 <= y < n):
        return True
    return False


def backtracking(cur_x, cur_y, coins, cnt):
    for i in range(4):
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        if is_in_range(nx, ny):
            if grid[nx][ny] == 'E':
                if len(coins) >= 3:
                    answer = min(answer, cnt)
                    return
            elif grid[nx][ny] != '.':
                if not coins:  # 첫 코인인 경우
                    coins.append(int(grid[nx][ny]))
                    backtracking(nx, ny, coins, cnt + 1)
                else:
                    if int(coins[-1]) < int(grid[nx][ny]):
                        if not visited[nx][ny]:
                            coins.append((int(grid[nx][ny])))
                            visited[nx][ny] = True
                            backtracking(nx, ny, coins, cnt + 1)
                            visited[nx][ny] = False
                    else:  # . 취급
                        backtracking(nx, ny, coins, cnt + 1)

            else:  # .
                backtracking(nx, ny, coins, cnt + 1)


if answer != INF:
    print(answer)
else:
    print(-1)