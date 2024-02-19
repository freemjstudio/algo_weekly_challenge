n, m = map(int, input().split())
arr = []

for _ in range(n):
    data = list(map(int, input().split()))
    arr.append(data)

answer = 0

for i in range(n):  # 가로
    count = 1
    max_count = 1
    for j in range(1, n):
        if arr[i][j - 1] == arr[i][j]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    if max_count >= m:
        answer += 1

for i in range(n):
    count = 1
    max_count = 1
    for j in range(1, n):
        if arr[j - 1][i] == arr[j][i]:
            count += 1
        else:
            count = 1
        max_count = max(count, max_count)
    if max_count >= m:
        answer += 1

print(answer)