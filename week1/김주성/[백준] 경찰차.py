### 문제 주소: https://www.acmicpc.net/problem/2618

import sys
sys.setrecursionlimit(10000)


def get_distance(case1, case2):
    d1 = case1[0]-case2[0]
    if d1 < 0:
        d1 = -d1
    d2 = case1[1]-case2[1]
    if d2 < 0:
        d2 = -d2
    return d1+d2


def dfs(i, j):
    if i == 1:
        return True

    if i-1 == j:
        for k in range(i):
            dist = get_distance(cases[i], cases[k])
            if dp[i-1][k] != -1 and dp[i][j]-dist == dp[i-1][k]:
                if dfs(i-1, k):
                    get_car_number([j, i])
                    return True
    else:
        dist = get_distance(cases[i], cases[i-1])
        if dp[i-1][j] != -1 and dp[i][j]-dist == dp[i-1][j]:
            if dfs(i-1, j):
                get_car_number([j, i])
                return True


def get_car_number(location):
    if car_location[0] in location:
        print(2)
        car_location[1] = location[1]
    else:
        print(1)
        car_location[0] = location[1]


input = sys.stdin.readline

N = int(input())
W = int(input())+2

cases = [(1, 1), (N, N)]

for _ in range(W-2):
    cases.append(tuple(map(int, input().split())))

dp = [[1e10 for _ in range(W)] for _ in range(W)]
dp[1][0] = 0

for i in range(1, W):
    for j in range(i):
        dist = get_distance(cases[i], cases[i-1])
        if dp[i][j] > dp[i-1][j]+dist:
            dp[i][j] = dp[i-1][j]+dist

        dist = get_distance(cases[i], cases[j])
        if dp[i][i-1] > dp[i-1][j]+dist:
            dp[i][i-1] = dp[i-1][j]+dist


min_move = 1e10
min_move_idx = -1
for i in range(W):
    if dp[-1][i] < min_move:
        min_move = dp[-1][i]
        min_move_idx = i

car_location = [0, 1]
print(min_move)
dfs(W-1, min_move_idx)