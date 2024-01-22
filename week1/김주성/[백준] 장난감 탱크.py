import sys
input = sys.stdin.readline

N = int(input())
moves = []
tanks = [list(map(int, input().split()))+[i] for i in range(1, N+1)]

tanks.sort()
up = []

for i in range(N, 0, -1):
    if tanks[i-1][0] > i:
        up.extend([str(tanks[i-1][2])+' U']*(tanks[i-1][0]-i))
    if tanks[i-1][0] < i:
        moves.extend([str(tanks[i-1][2])+' D']*(i-tanks[i-1][0]))

moves += up[::-1]
tanks.sort(key=lambda x: x[1])

for i in range(N, 0, -1):
    if tanks[i - 1][1] > i:
        moves.extend([str(tanks[i - 1][2]) + ' L'] * (tanks[i - 1][1] - i))
    if tanks[i - 1][1] < i:
        moves.extend([str(tanks[i - 1][2]) + ' R'] * (i - tanks[i - 1][1]))

print(len(moves), *moves, sep='\n')