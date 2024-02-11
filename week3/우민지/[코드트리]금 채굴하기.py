n, m = map(int, input().split())
array = []
for _ in range(n):  # n * n 영역
    array.append(list(map(int, input().split())))

def check_gold(x, y, s):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if abs(x - i) + abs(y - j) <= s:
                cnt += array[i][j]
    return cnt

def get_block(s):  # 마름모 넓이에 속한 block (1*1) 개수 반환
    return s * s + (s + 1) * (s + 1)


answer = 0

for i in range(n):
    for j in range(n):
        # i, j 중심으로 상하좌우를 확인
        for s in range(2 * (n - 1) + 1):  # 임의로 늘린 것 ?
            cnt = check_gold(i, j, s)
            if cnt * m >= get_block(s):
                answer = max(answer, cnt)

print(answer)