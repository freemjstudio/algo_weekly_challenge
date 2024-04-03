import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(node, root):
    global time
    time += 1
    discover[node] = time
    ret = discover[node]
    child = 0
    for next_node in graph[node]:
        if discover[next_node] == 0:
            child += 1
            df = dfs(next_node, 0)
            if not root and df >= discover[node]:
                cut[node] = True
            ret = min(ret, df)
        else:
            ret = min(ret, discover[next_node])
    if root and child > 1:
        cut[node] = True
    return ret


V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

discover = [0] * (V+1)
cut = [False] * (V+1)
time = 0
answer = 0
for i in range(1, V+1):
    if discover[i] == 0:
        dfs(i, True)
for i in range(1, V+1):
    if cut[i]:
        answer += 1
print(answer)
for i in range(1, V+1):
    if cut[i]:
        print(i, end=' ')