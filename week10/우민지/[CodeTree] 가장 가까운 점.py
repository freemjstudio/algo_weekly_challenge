import heapq

n, m = map(int, input().split())

pq = []

# 초기 입력
for i in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, ((abs(x) + abs(y)),x, y))

for i in range(m):
    dist , min_x, min_y = heapq.heappop(pq) # 원점에서 가장 가까운 점
    min_x += 2
    min_y += 2
    dist = abs(min_x) + abs(min_y)
    heapq.heappush(pq, (dist , min_x, min_y))


dist, min_x, min_y = heapq.heappop(pq)
print(min_x, min_y)