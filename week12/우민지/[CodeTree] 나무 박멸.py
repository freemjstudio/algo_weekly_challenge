# https://www.codetree.ai/training-field/frequent-problems/problems/tree-kill-all/description?page=1&pageSize=20
n, m, k, C = map(int, input().split())

grid = []
tree_pos = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] > 0:
            tree_pos.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 대각선 이동
tx = [-1, 1, -1, 1]
ty = [-1, 1, 1, -1]


# 성장
def grow():
    global tree_pos
    temp = [[0] * n for _ in range(n)]
    for x, y in tree_pos:
        tree_cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] > 0:
                    tree_cnt += 1
        temp[x][y] = tree_cnt
    # grow 적용
    for x in range(n):
        for y in range(n):
            grid[x][y] += temp[x][y]

        # 번식 - 번식 가능한 칸의 개수 만큼 번식됨


def spread():
    global tree_pos
    temp = [[0] * n for _ in range(n)]
    for x, y in tree_pos:
        vacant_cnt = 0
        vacant_pos = []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 0:
                    vacant_cnt += 1
                    vacant_pos.append((nx, ny))  # 번식할 수 있는 칸의 위치

        for r, c in vacant_pos:
            temp[r][c] += grid[x][y] // vacant_cnt

    tree_pos = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] > 0 or temp[x][y] > 0:
                tree_pos.append((x, y))
                grid[x][y] += temp[x][y]


kill_pos = []


# 제초제 위치 구하기
def get_kill_pos():
    global kill_pos

    max_kill = 0
    r, c = -1, -1  # max kill 값의 위치를 구하기 (제초제 뿌릴 위치)
    tree_pos.sort()  # 행, 열 순으로 정렬하기
    for x, y in tree_pos:
        kill_count = grid[x][y]  # 자기 자신의 위치 나무 박멸

        for t in range(4):
            nx, ny = x, y
            for _ in range(k):  # 대각선 방향 K 까지 영향줌
                nx += tx[t]
                ny += ty[t]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1:
                    kill_count += grid[nx][ny]
                else:  # 범위 벗어나면 확산 중단
                    break
        if max_kill < kill_count:
            max_kill = kill_count
            r, c = x, y
    kill_pos.append((r, c, C))


# 박멸 진행하기 -> 아직 유효한 제초제 위치에 대해서만 작업하기
def kill_tree():
    global answer
    update_kill_pos = []
    for kp in kill_pos:
        r, c, C = kp
        if C <= 0:
            grid[r][c] = 0  # 제초제 삭제
            continue
        if grid[r][c] > 0:
            answer += grid[r][c]
            grid[r][c] == -2  # 제초제 처리
            C -= 1
        # kill 진행
        for t in range(4):
            nx, ny = r, c
            for _ in range(k):
                nx += tx[t]
                ny += ty[t]
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1:
                    answer += grid[nx][ny]
                    grid[nx][ny] = 0
                else:
                    break

        update_kill_pos.append((r, c, C))

    kill_pos = update_kill_pos


for _ in range(m):
    grow()
    spread()
    get_kill_pos()
    kill_tree()

print(answer)