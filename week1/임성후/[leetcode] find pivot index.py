class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)
        for m in range(len(nums)):
            if sum(nums[left: m]) == sum(nums[m+1: right]):
                return m
        else:
            return -1


s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([1, 2, 3]))
