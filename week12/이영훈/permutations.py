from itertools import permutations
from types import List 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))