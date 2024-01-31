n = str(input())
arr = []
for num in n:
    arr.append(int(num))

answer = arr[0]

for i in range(1, len(arr)):
    if arr[i] <= 1:
        answer += arr[i]
    else:
        if answer <= 1:
            answer += arr[i]
        else:
            answer *= arr[i]

print(answer)