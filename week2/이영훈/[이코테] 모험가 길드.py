n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
count = 0

for x in arr:
    count += 1
    if count >= x:
        answer += 1
        count = 0

print(answer)
