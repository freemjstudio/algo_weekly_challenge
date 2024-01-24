class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count, ans, i, j = 0, 0, 0, 0

        while j < len(nums):
            if nums[j] == 0:
                count += 1

            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans