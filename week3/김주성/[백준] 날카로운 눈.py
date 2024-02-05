import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

s = 1
e = 2147483647

odd_num = -1
count = 0
while s <= e:
    mid = (s+e)//2
    n = 0
    for i in range(N):
        if arr[i][0] <= mid:
            max_num = min(mid, arr[i][1])
            n += (max_num-arr[i][0])//arr[i][2]+1
    if n % 2 == 0:
        s = mid+1
    else:
        e = mid-1
        odd_num = mid

for i in range(N):
    if arr[i][0] <= odd_num <= arr[i][1]:
        if (odd_num - arr[i][0]) % arr[i][2] == 0:
            count += 1

if odd_num == -1:
    print('NOTHING')
else:
    print(odd_num, count)