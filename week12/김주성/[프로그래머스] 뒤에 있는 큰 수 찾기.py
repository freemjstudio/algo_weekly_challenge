def solution(numbers):
    answer = []
    stack = []
    for number in numbers[::-1]:
        while stack and stack[-1]<=number:
            stack.pop()
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack[-1])
        stack.append(number)
    return answer[::-1]