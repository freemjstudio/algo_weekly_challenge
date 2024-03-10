n, m, q = map(int, input().split()) # n * m
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def left_shift(row):
    temp = arr[row][-1]
    for i in range(n-1, -1, -1):
        arr[row][i] = arr[row][i-1]
    arr[row][0] = temp
    r = row
    # up
    while r >= 0:
        if check_line_up(r, r-1) and (r-1) >= 0: # true
            r -= 1
            temp = arr[r][-1]
            for i in range(n-1, -1, -1):
                arr[r][i] = arr[r][i-1]
            arr[r][0] = temp
        else:
            break
    r = row
    # down
    while r < n:
        if check_line_down(r, r+1) and (r+1) < n:
            r += 1

            temp = arr[r][-1]
            for i in range(n-1, -1, -1):
                arr[r][i] = arr[r][i-1]
            arr[r][0] = temp
# 오른쪽에서 미는 경우
def right_shift(row):
    temp = arr[row][0]
    for i in range(1, n):
        arr[row][i-1] = arr[row][i]
    arr[row][-1] = temp
    r = row
    while r >= 0:
        if check_line_up(r, r-1) and (r-1) >= 0:
            r -= 1
            temp = arr[r][0]
            for i in range(1, n):
                arr[r][i-1] = arr[r][i]
            arr[r][-1] = temp
    while r < n:
        if check_line_down(r, r+1) and (r-1) < n:
            r += 1
            temp = arr[r][0]
            for i in range(1, n):
                arr[r][i-1] = arr[r][i]
            arr[r][-1] = temp



def check_line_up(r1, r2):
    for i in range(n):
        if arr[row][i] == arr[row-1][i]:
            return True
    return False

def check_line_down(r1, r2):
    for i in range(n):
        if arr[row][i] == arr[row+1][i]:
            return True
    return False

def check_line_down(r1, r2):

for _ in range(q):
    r, d = input().split()
    r = int(r)
    if d == 'L':
        left_shift(r)
    else:
        right_shift(r)

for a in arr:
    print(*a)