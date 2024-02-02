def solution(triangle):
    answer = 0
    dp = []
    n = len(triangle)
    for i in range(n):
        dp.append([0] * (i+1))
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            elif i-1 >= 0 and j-1 >= 0:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])


    return max(dp[-1])

# tc
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
answer = solution(triangle)
print(answer)