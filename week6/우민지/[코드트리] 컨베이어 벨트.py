n, t = map(int, input().split())
arr = []

for _ in range(2):
    arr.append(list(map(int, input().split())))

# 오른쪽으로 shift
temp = arr[0][n-1] # 3
for i in range(n-1, 0, -1):
    arr[0][i] = arr[0][i-1]
# 아래로 shift
temp2 = arr[1][n-1]
arr[1][n-1] = temp

temp3 = arr[1][0]
# 왼쪽으로 shift
for i in range(n-2, 0, -1):
    arr[1][i-1] = arr[1][i]

# 위로 shift
arr[0][0] = temp3

# print
for i in range(2):
    print(*arr[i])