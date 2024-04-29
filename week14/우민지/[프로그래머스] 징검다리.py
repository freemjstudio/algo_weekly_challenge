def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()
    left, right = 0, distance

    while left <= right:
        mid = (left + right) // 2
        remove_rock_cnt = 0  # 제거한 바위 수

        prev_rock = 0
        for rock in rocks:
            if (rock - prev_rock) < mid:  # 기준보다 작으면 제거하기 (기준은 거리의 최솟값임)
                remove_rock_cnt += 1
                if remove_rock_cnt > n:  # 이미 초과해서 제거한 경우 fail 이므로 멈추기
                    break
            else:
                prev_rock = rock  # 갱신하기

        if remove_rock_cnt > n:  # 너무 많이 삭제 -> mid 커트라인이 너무 높다
            right = mid - 1
        else:
            answer = max(answer, mid)
            left = mid + 1

    return answer