# https://school.programmers.co.kr/learn/courses/30/lessons/43236

from itertools import combinations


def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    comb = combinations(rocks, len(rocks) - n)

    # 모든 경우 확인
    for com in comb:
        min_dist = distance
        for i in range(len(com)):
            if i == 0:
                min_dist = min(min_dist, com[i])
            elif i == len(com) - 1:
                min_dist = min(min_dist, distance - com[i])
            else:
                min_dist = min(min_dist, com[i] - com[i - 1])

        answer = max(min_dist, answer)

    return answer