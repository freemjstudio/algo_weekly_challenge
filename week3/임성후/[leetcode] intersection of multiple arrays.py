class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = list(set(temp) & set(nums[i]))
        return sorted(temp)


s = Solution()
s.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]])
