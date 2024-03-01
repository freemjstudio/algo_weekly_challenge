import sys
input = sys.stdin.readline

n = int(input())
x, y = (map(int, input().split()))
grid = []
# 시계 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0
dir_idx = 0 # 현재 방향 기록

for _ in range(n):
    grid.append(list(input()))
# 방향 체크 + 현재 위치에 온적 있는지 여부 체크
visited = [[[False] * 4 for _ in range(n)] for _ in range(n)]
def is_in_range(i, j):
    return (0 <= i < n) and (0 <= j < n)
# 벽이 있는지 확인
def is_wall(i, j):
    return is_in_range(i, j) and grid[i][j] == '#'

cur_x, cur_y = x-1, y-1

def simulate():
    global cur_x, cur_y, answer, dir_idx, dx, dy

    if not visited[cur_x][cur_y][dir_idx]:
        answer = -1
        return

    visited[cur_x][cur_y][dir_idx] = True
    nx, ny = cur_x + dx[dir_idx], cur_y + dy[dir_idx]
    if is_wall(nx, ny): # step 1 - 반시계 방향
        dir_idx = (dir_idx+3) % 4
    elif not is_in_range(nx, ny): # step2 - case 1 - 탈출
        answer += 1
        cur_x, cur_y = nx, ny
    else:
        # 오른쪽 칸 확인
        right_dir = (dir_idx+3) % 4
        rx, ry = nx + dx[right_dir], ny + dy[right_dir]

        if is_wall(rx, ry):
            cur_x, cur_y = nx, ny
            answer += 1
        else:
            # 한 칸 이동 + 90도 회전 + 한 칸 이동
            cur_x, cur_y = rx, ry
            dir_idx = (dir_idx+1) % 4
            answer += 2


while is_in_range(cur_x, cur_y):
    simulate()

print(answer)