def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    left, right = 0, 10000

    while left <= right:
        mid = (left+right)//2
        # h 번 이상 인용된 논문이 h 편인지 확인
        count = 0
        for i in range(n):
            if citations[i] >= mid:
                count += 1
        if count >= mid:
            answer = max(mid, answer)
            left = mid + 1
             # h-index
        else:
            right = mid-1

    return answer

c = [3, 0, 6, 1, 5]
answer = solution(c)
print(answer)