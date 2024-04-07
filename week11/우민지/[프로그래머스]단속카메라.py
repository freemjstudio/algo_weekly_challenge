def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])
    # print(routes)
    last = -30001

    for route in routes:
        if route[0] > last:
            answer += 1
            last = route[1]

    return answer