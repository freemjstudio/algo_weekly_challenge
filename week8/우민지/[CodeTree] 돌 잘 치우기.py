from collections import deque
import sys

input = sys.stdin.readline
n, k, m = map(int, input().split())

arr = []
rocks = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            rocks.append((i, j))
    arr.append(line)

start_pos = []
for _ in range(k):
    r, c = map(int, input().split())
    start_pos.append((r - 1, c - 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
visited = [[False] * n for _ in range(n)]


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True


queue = deque()
selected_rocks = []  # 제거할 위치 돌 m 개 선택


def simulate():
    for x, y in selected_rocks:
        arr[x][y] = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for sx, sy in start_pos:
        queue.append((sx, sy))
        visited[sx][sy] = True

    bfs()
    # 다시 복구하기
    for x, y in selected_rocks:
        arr[x][y] = 1
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1
    return count


# backtracking
def find_max(idx, cnt):
    global answer

    if idx == len(rocks):
        if cnt == m:
            answer = max(answer, simulate())
        return

    selected_rocks.append(rocks[idx])
    find_max(idx + 1, cnt + 1)
    selected_rocks.pop()
    find_max(idx + 1, cnt)


find_max(0, 0)
print(answer)