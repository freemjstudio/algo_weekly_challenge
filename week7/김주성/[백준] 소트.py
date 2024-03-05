N = int(input())

arr = tuple(map(int, input().split()))
nums_dict = {}
for num in arr:
    if num not in nums_dict:
        nums_dict[num] = 0
    nums_dict[num] += 1

answer = [-2]
while len(nums_dict) > 0:
    if len(nums_dict) == 2:
        num1, num2 = nums_dict.keys()
        if num1 > num2:
            num1, num2 = num2, num1
        if num1+1 == num2:
            answer += [num2]*nums_dict[num2]
            answer += [num1]*nums_dict[num1]
            break

    for i in range(1001):
        if i == answer[-1]+1:
            continue
        if i in nums_dict:
            answer.append(i)
            nums_dict[i] -= 1
            if nums_dict[i] == 0:
                nums_dict.pop(i)
            break
print(*answer[1:])