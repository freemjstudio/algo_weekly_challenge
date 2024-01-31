# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    n = len(routes)
    answer = 0 # 최소

    routes.sort(key = lambda x:x[1])
    checkpoint = -30001

    for start, end in routes:
        if start > checkpoint:
            answer += 1
            checkpoint = end # 새로운 기준

    return answer

# tc
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
answer = solution(routes)
print(answer)