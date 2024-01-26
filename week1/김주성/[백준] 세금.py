import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M, K = map(int, input().split())
S, D = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append(tuple([b, w]))
    graph[b].append(tuple([a, w]))

fee_raise = [0]+[int(input()) for _ in range(K)]

path = [[-1 for _ in range(N+1)] for _ in range(N+1)]
path[S][0] = 0
heap = [(0, S, 0)]

while heap:
    total_fee, node, count = heapq.heappop(heap)
    for next_node, fee in graph[node]:
        forward = True
        for i in range(count+2):
            if path[next_node][i] != -1 and path[next_node][i] <= total_fee+fee:
                forward = False
                break
        if forward:
            path[next_node][count+1] = total_fee+fee
            heapq.heappush(heap, (total_fee+fee, next_node, count+1))

for raising in fee_raise:
    min_fee = 1e9
    for i in range(N+1):
        if path[D][i] != -1:
            path[D][i] += i*raising
            if min_fee > path[D][i]:
                min_fee = path[D][i]
    print(str(min_fee)+'\n')