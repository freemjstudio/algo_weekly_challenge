class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = []
        for t in s:
            if t.isalpha() or t.isdigit():
                temp.append(t)

        if temp == temp[::-1]:
            return True
        
        return False 
        