n = int(input())
arr = list(map(int, input().split()))

arr.sort()

target = 1

for x in arr:
    if x > target:
        break 
    target += x 

print(target)