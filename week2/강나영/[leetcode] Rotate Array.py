class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k %= len(nums)
        
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
                
        r = len(nums) - 1
        
        reverse(nums, 0, r)
        reverse(nums, 0, k-1)
        reverse(nums, k, r)