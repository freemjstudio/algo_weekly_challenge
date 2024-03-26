# https://www.codetree.ai/missions/8/problems/nearest-point/description

import heapq

n, m = map(int, input().split())

pq = []

# 초기 입력
for i in range(n):
    x, y = map(int, input().split())
    heapq.heappush(pq, ((abs(x) + abs(x)),x, y))

for i in range(m):
    _ , min_x, min_y = heapq.heappop(pq)
    min_x, min_y = min_x + 2, min_y + 2
    heapq.heappush(pq, (abs(min_x) + abs(min_y) , min_x, min_y))

_, min_x, min_y = heapq.heappop(pq)
print(min_x, min_y)