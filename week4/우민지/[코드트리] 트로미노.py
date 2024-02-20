n, m = map(int, input().split())
grid = []
answer = 0
for i in range(n):
    grid.append(list(map(int, input().split())))

types = [
    [[1, 1, 0],
     [1, 0, 0],
     [0, 0, 0]],

    [[1, 1, 0],
     [0, 1, 0],
     [0, 0, 0]],

    [[1, 0, 0],
     [1, 1, 0],
     [0, 0, 0]],

    [[0, 1, 0],
     [1, 1, 0],
     [0, 0, 0]],

    [[1, 1, 1],
     [0, 0, 0],
     [0, 0, 0]],

     [[1, 0, 0],
     [1, 0, 0],
     [1, 0, 0]]
]

# type 별로 탐색하기 & 최대합 구하기
def solve(x, y):
    max_total = 0 # max value
    for i in range(6):
        flag = True # 범위 확인
        temp_total = 0
        for dx in range(3):
            for dy in range(3):
                if types[i][dx][dy] == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m: # 범위 check
                    temp_total += grid[nx][ny]
                else:
                    flag = False
        if flag:
            max_total = max(temp_total, max_total)
    return max_total


# 3*1 block
for x in range(n):
    for y in range(m):
        answer = max(answer, solve(x, y))
print(answer)