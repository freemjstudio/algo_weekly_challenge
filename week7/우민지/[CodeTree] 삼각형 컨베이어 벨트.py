n, t = map(int, input().split())

left = list(map(int, input().split()))
right = list(map(int, input().split()))
down = list(map(int, input().split()))

# t 초 반복
for _ in range(t):

    temp = left[-1]
    for i in range(n-1, 0, -1):
        left[i] = left[i-1]
    temp2 = right[-1]
    for i in range(n-1, 0, -1):
        right[i] = right[i-1]
    right[0] = temp
    temp3 = down[-1]
    for i in range(n-1, 0, -1):
        down[i] = down[i-1]

    down[0] = temp2
    left[0] = temp3
print(*left)
print(*right)
print(*down)