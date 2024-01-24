class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)
        answer = [1 for _ in range(N)]
        for i in range(1, N):
            answer[i] = answer[i-1] * nums[i-1]
        # print(answer) # left -> right
        temp = 1
        # right -> left
        for i in range(N-2, -1, -1):
            temp *= nums[i+1]
            answer[i] *= temp

        return answer

# Test Case
s = Solution()
answer = s.productExceptSelf(nums=[1,2,3,4])
print(answer)