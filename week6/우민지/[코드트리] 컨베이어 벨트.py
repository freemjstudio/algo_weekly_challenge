n, t = map(int, input().split())
arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))


for _ in range(t):
# 오른쪽으로 shift
    temp = arr[0][n-1] # 가장 오른쪽에 있는 숫자
    for i in range(n-1, 0, -1):
        arr[0][i] = arr[0][i-1]

    arr[0][0] = arr[1][n-1]

    for i in range(n-1, 0, -1):
        arr[1][i] = arr[1][i-1]

    arr[1][0] = temp

# print result
for i in range(2):
    print(*arr[i])