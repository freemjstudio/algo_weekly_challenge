import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower()
        strs = re.sub('[^a-z0-9]', '', strs)
        return strs == strs[::-1]
