# LeetCode Top Interview 150

# Category: Array
# Title: Best Time to Buy and Sell Stock II

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                answer += (prices[i] - prices[i-1])
        return answer