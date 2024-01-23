# LeetCode Top Interview 150

# Category: 1D DP
# Title: 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second
