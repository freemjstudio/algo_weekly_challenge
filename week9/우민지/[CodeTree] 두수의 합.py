
n, k = map(int, input().split())
arr = list(map(int, input().split()))

numbers = dict()

answer = 0

for elem in arr:
    diff = (k - elem)

    # 가능한 쌍의 수
    if diff in numbers:
        answer += numbers[diff]
    if elem in numbers:
        numbers[elem] += 1
    else:
        numbers[elem] = 1 # initlaize


print(answer)