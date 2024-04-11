from types import List 
from itertools import combinations

# My solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        for i in range(len(nums)+1):
            comb = list(combinations(nums, i))
            for c in comb:
                results.append(c)

        return results

# Basic solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(index, path):
            results.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])
        return results
        