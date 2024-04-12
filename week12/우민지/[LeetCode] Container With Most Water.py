# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0

        left, right = 0, len(height) - 1

        while left < right:

            h = min(height[left], height[right])

            water = (right - left) * h

            answer = max(answer, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return answer