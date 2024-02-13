n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

ball = [0] * 11
result = 0

for i in arr:
    ball[i] += 1

for i in range(1, m+1):
    n -= ball[i]
    result += n * ball[i]

print(result)
