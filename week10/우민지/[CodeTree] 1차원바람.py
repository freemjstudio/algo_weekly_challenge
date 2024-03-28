n, m, q = map(int, input().split())  # n * m
arr = []

for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)


def shift_left(row):  # 왼쪽에서 미는 경우 (오른쪽으로 한칸씩 이동)
    temp = arr[row][-1]  # 맨 마지막 칸

    for i in range(m - 2, -1, -1):
        arr[row][i + 1] = arr[row][i]
    arr[row][0] = temp


def shift_right(row):  # 오른쪽에서 미는 경우 (왼쪽으로 한칸씩 이동)
    temp = arr[row][0]
    for i in range(0, m - 1, 1):
        arr[row][i] = arr[row][i + 1]
    arr[row][-1] = temp


def check_up_line(row):  # 현재 column
    if row >= n - 1:
        return False
    for col in range(n):
        if arr[row][col] == arr[row + 1][col]:
            return True


def check_down_line(row):
    if row <= 0:
        return False
    for col in range(n):
        if arr[row][col] == arr[row - 1][col]:
            return True


def simulate(start_row, wind_dir):
    if wind_dir == "L":  # left 진행
        print()
    else:  # right shift
        print("right")


def print_result():
    for i in range(n):
        print(*arr[i])


for _ in range(q):
    row, wind_dir = input().split()
    row = int(row) - 1
    # simulate(col, wind_dir)
shift_right(row)
print_result()