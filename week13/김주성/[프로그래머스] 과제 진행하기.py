def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)):
        t, m = plans[i][1].split(':')
        plans[i][1] = int(t) * 60 + int(m)

    stack = []

    for i in range(len(plans)):
        stack.append([plans[i][0], int(plans[i][2])])
        if i + 1 == len(plans):
            while stack:
                answer.append(stack.pop()[0])
            break
        now = plans[i][1]
        while stack:
            if now + stack[-1][1] <= plans[i + 1][1]:
                task, time = stack.pop()
                answer.append(task)
                now += time
            else:
                stack[-1][1] -= plans[i + 1][1] - now
                break
    return answer