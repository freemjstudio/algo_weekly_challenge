class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        count = -1
        for i, v in enumerate(word):
            if v == ch:
                count = i
                break
        if count != -1:
            return ''.join(list(word[0: count + 1])[::-1]) + word[count + 1:]
        return word
    
s = Solution()

print(s.reversePrefix("abcdefd", "d"))
print(s.reversePrefix("xyxzxe", "z"))
print(s.reversePrefix("abcd", "z"))
