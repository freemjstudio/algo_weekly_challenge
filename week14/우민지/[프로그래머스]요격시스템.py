# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])
    last = targets[0][1]  # 구간 사이에서 요격해야 함

    for s, e in targets[1:]:
        if last > s:
            continue
        else:
            answer += 1
            last = e

    return answer