# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque


def solution(n, wires):
    answer = 100

    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for wire in wires:
        i, j = wire
        graph[i][j] = 1
        graph[j][i] = 1

    # 해당 전력망의 송전탑 개수 반환
    def bfs(node):
        visited = [False] * (n + 1)
        count = 0
        queue = deque()
        queue.append(node)
        visited[node] = True

        while queue:
            now = queue.popleft()
            count += 1
            for next in range(1, n + 1):
                if graph[now][next] and not visited[next]:  # 연결이 있는 경우
                    queue.append(next)
                    visited[next] = True

        return count

        # 연결을 하나씩 끊어보는 경우

    for wire in wires:
        i, j = wire
        graph[i][j] = 0
        graph[j][i] = 0
        cnt1 = bfs(i)
        cnt2 = bfs(j)
        answer = min(abs(cnt1 - cnt2), answer)
        graph[i][j] = 1
        graph[j][i] = 1

    return answer