# https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20

L, N, Q = map(int, input().split())

grid = []
for _ in range(L):
    line = input().split()
    grid.append(line)

nights = [[0] * L for _ in range(L)] # 체스판을 하나 더 만들기
pos = {}
for idx in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    pos[idx] = []
    # 체력 표시하기
    for i in range(r, r+h):
        for j in range(c, c+w):
            nights[i][j] = k
            pos[idx].append((i, j))

'''
0 5 0 0
1 5 0 0
1 3 3 0
0 0 0 0
'''
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왕의 명령에 대한 정보
for _ in range(Q):
    i, d = map(int, input().split())