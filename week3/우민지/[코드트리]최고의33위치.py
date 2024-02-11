N = int(input())

graph = []
answer = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

def get_coin_num(r1, c1):
    cnt = 0
    for i in range(r1, r1+3):
        for j in range(c1, c1+3):
            cnt += graph[i][j]
    return cnt

for i in range(N):
    for j in range(N):
        if 0 <= (i + 2) < N and 0 <= (j+2) < N:
            answer = max(answer, get_coin_num(i, j))

print(answer)