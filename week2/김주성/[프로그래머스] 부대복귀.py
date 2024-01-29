from collections import deque
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    dist = [-1] * (n+1)
    dist[destination] = 0
    for node1, node2 in roads:
        graph[node1].append(node2)
        graph[node2].append(node1)
    q=deque([destination])
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node]+1
                q.append(next_node)
    return [dist[s] for s in sources]