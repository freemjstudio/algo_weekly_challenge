class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0
        for a in range(0, len(nums) - 1):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] < target:
                    count += 1
                    
        return count


s = Solution()

print(s.countPairs([-1, 1, 2, 3, 1], 2))
print(s.countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
