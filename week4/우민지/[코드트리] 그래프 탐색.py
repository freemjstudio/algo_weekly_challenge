n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = 0
visited = [False] * (n + 1)


def dfs(now):
    global answer
    for x in graph[now]:
        if not visited[x]:
            answer += 1
            visited[x] = True
            dfs(graph[x])


visited[1] = True
dfs(1)

print(answer)