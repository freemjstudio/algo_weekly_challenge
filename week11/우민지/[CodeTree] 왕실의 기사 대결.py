from collections import deque

L, N, Q = map(int, input().split())
# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

MAX_N = 31  # 기사의 수
MAX_L = 41  # 체스판의 크기

info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
before_k = [0 for _ in range(MAX_N)]  # 원래의 체력
r = [0 for _ in range(MAX_N)]
c = [0 for i in range(MAX_N)]
h = [0 for i in range(MAX_N)]
w = [0 for i in range(MAX_N)]
k = [0 for i in range(MAX_N)]  # 나중의 체력 (데미지 계산용)

# new
nr = [0 for i in range(MAX_N)]
nc = [0 for i in range(MAX_N)]
damage = [0 for i in range(MAX_N)]
is_moved = [False for _ in range(MAX_N)]

answer = 0


def simulate(idx, d):
    queue = deque()
    is_pos = True

    # reset
    for i in range(1, N + 1):
        damage[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]
    queue.append(idx)  # 기사 번호
    is_moved[idx] = True  # 기사 움직이기

    while queue:
        x = queue.popleft()
        nr[x] += dx[d]
        nc[x] += dy[d]
        # 체스판 넘어가는지 확인
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] - 1 > L or nc[x] + w[x] - 1 > L:
            return False

        for i in range(nr[x], nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:  # 함정
                    damage[x] += 1
                if info[i][j] == 2:  # 벽 -> 이동 불가능
                    return False

                    # 다른 조각과 충돌
        for i in range(1, N + 1):
            if is_moved[i] or k[i] <= 0:
                continue
            if r[i] > (nr[x] + h[x] - 1) or (nr[x] > r[i] + h[i] - 1):
                continue
            if c[i] > (nc[x] + w[x] - 1) or (nc[x] > c[i] + w[i] - 1):
                continue

            is_moved[i] = True
            queue.append(i)  # queue 를 이용하여 연쇄적으로 처리하기
    damage[idx] = 0
    return True


def move(idx, d):  # idx , dir
    if k[idx] <= 0:
        return

    if simulate(idx, d):  # 이동 가능 체크
        for i in range(1, N + 1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= damage[i]


for i in range(1, L + 1):
    info[i][1:] = map(int, input().split())

for i in range(1, N + 1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    before_k[i] = k[i]

for _ in range(Q):
    idx, d = map(int, input().split())
    move(idx, d)

answer = 0
for i in range(1, N + 1):
    # 생존한 기사들만 데미지 확인
    if k[i] > 0:
        answer += before_k[i] - k[i]

print(answer)