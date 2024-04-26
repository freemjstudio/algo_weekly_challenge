class Solution:
    def longestPalindrome(self, s: str) -> str:

        # My solution - 완전탐색을 통한 시간복잡도 O(n^2)
        # answer = ''
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             temp = s[i:j+1]
        #             if len(temp) > len(answer):
        #                 answer = temp

        # return answer

        # Book Solution - 투포인터를 활용한 시간 복잡도 O(n)
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result