n = int(input())
m = 3  # 동전은 최소 3개

grid = []
INF = int(1e9)
answer = INF
s = (0, 0)  # start
e = (n - 1, n - 1)  # end

coin_pos = []  # 동전의 위치, 오름차순 정렬
selected_pos = []  # 선택한 동전
for i in range(n):
    line = list(input())
    for j in range(n):
        if line[j] == 'S':
            s = (i, j)
        if line[j] == 'E':
            e = (i, j)

    grid.append(line)

# 동전 오름차순으로 위치 넣기
for num in range(1, 10):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == str(num):
                coin_pos.append((i, j))


def get_dist(a, b):
    (ax, ay) = a
    (bx, by) = b
    return abs(ax - bx) + abs(ay - by)


def calc():
    temp = get_dist(s, selected_pos[0])
    for i in range(m - 1):
        temp += get_dist(selected_pos[i], selected_pos[i + 1])
    temp += get_dist(selected_pos[m - 1], e)
    return temp


def backtracking(idx, cnt):  # coin index, cnt
    global answer

    if cnt == m:
        answer = min(answer, calc())
        return
    if idx == len(coin_pos):  # 코인 모든 조합 탐색 완료
        return
        # 선택하지 않은 경우
    backtracking(idx + 1, cnt)

    # 선택한 경우
    selected_pos.append(coin_pos[idx])
    backtracking(idx + 1, cnt + 1)
    selected_pos.pop()  # back


backtracking(0, 0)
if answer == INF:
    answer = -1
print(answer)