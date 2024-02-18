n, m = map(int, input().split())
grid = []
answer = 0
for i in range(n):
    grid.append(list(map(int, input().split())))

# 3*1 block
for x in range(n):
    for y in range(m):
        # 가로
        if 0 <= (x + 2) < n and 0 <= (y + 2) < m:

    # 세로

print(answer)