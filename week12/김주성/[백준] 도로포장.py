from heapq import heappush, heappop
from math import inf
from sys import stdin

input = stdin.readline

N, M, K = map(int, input().split())

times = [[inf for _ in range(K+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for i in range(K+1):
    times[1][i] = 0

for _ in range(M):
    n1, n2, time = map(int, input().split())
    graph[n1].append([n2, time])
    graph[n2].append([n1, time])

heap = [(0, 1, 0)]

while heap:
    time, node, pave = heappop(heap)
    if times[node][pave] < time:
        continue
    for next_node, travel_time in graph[node]:
        if times[next_node][pave] > time+travel_time:
            heappush(heap, (time+travel_time, next_node, pave))
            times[next_node][pave] = time+travel_time
        if pave+1 <= K:
            if times[next_node][pave+1] > time:
                heappush(heap, (time, next_node, pave+1))
                times[next_node][pave+1] = time
print(min(times[N]))