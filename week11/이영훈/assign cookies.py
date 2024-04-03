from types import List 

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        answer = 0
        for greed in g:
            for i in range(len(s)):
                if s[i] >= greed:
                    answer += 1
                    s.pop(i)
                    break

        return answer
        