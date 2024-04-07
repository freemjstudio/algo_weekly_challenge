# https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20
from collections import deque

L, N, Q = map(int, input().split())
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

grid = []
nights = {}
answer = 0


class Night():
    def __init__(self, idx, r, c, h, w, k):
        self.idx = idx
        self.r = r
        self.c = c
        self.h = h
        self.w = w
        self.k = k


for _ in range(L):
    line = list(map(int, input().split()))
    grid.append(line)

for idx in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    nights[idx] = Night(idx, r, c, h, w, k)


def check_avalible(now, d):
    flag = True
    # bfs 진행하기
    queue = deque()
    queue.append(now)
    while queue:
        now = queue.popleft()
        for i in range():

    return flag


def update_info():
    global answer  # 업데이트하면서 피해량 구하기


def simulate(idx, d):
    global answer
    # 해당 기사 찾기
    now = nights[idx]
    if now.k > 0:  # 아직 살아 있는지 확인


# 밀칠 수 있는지 여부 확인

# 밀치기 , 좌표와 체력 업데이트 연쇄적으로 하기

# 피해량을 구하기

for _ in range(Q):
    idx, d = map(int, input().split())
    simulate(idx, d)

print(answer)