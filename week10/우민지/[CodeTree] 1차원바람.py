
n, m, q = map(int, input().split()) # n * m
arr = []

SHIFT_RIGHT = 0
SHIFT_LEFT = 1

for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)

def shift(row, cur_dir):
    if cur_dir == SHIFT_RIGHT: # 오른쪽으로 밀어야 하는 경우
        arr[row].insert(0, arr[row].pop())
    else:
        arr[row].insert(m-1, arr[row].pop(0))

def check_same_num(row1, row2):
    for col in range(m):
        if arr[row1][col] == arr[row2][col]:
            return True
    return False

def flip_dir(cur_dir):
    return SHIFT_RIGHT if cur_dir == SHIFT_LEFT else SHIFT_LEFT

def simulate(start_row, start_dir):
    shift(start_row, start_dir)
    start_dir = flip_dir(start_dir)

    # 전파 시키기 - 위 방향
    cur_dir = start_dir

    for row in range(start_row, 0, -1):
        if check_same_num(row, row-1):
            shift(row-1, cur_dir)
            cur_dir = flip_dir(cur_dir)
        else:
            break

    # 전파 시키기 - 아래 방향
    cur_dir = start_dir
    for row in range(start_row, n-1):
        if check_same_num(row, row+1):
            shift(row+1, cur_dir)
            cur_dir = flip_dir(cur_dir)
        else:
            break

def print_result():
    for i in range(n):
        print(*arr[i])

for _ in range(q):
    row, wind_dir = input().split()
    row = int(row) - 1
    if wind_dir == 'L':
        cur_dir = SHIFT_RIGHT
    else:
        cur_dir = SHIFT_LEFT
    simulate(row, cur_dir)

print_result()