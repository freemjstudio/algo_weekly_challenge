class Solution:
    def reverseWords(self, s: str):
        return " ".join(s.split()[::-1])


