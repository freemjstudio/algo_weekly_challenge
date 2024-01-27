from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = Counter(word1)
        dict2 = Counter(word2)
        if set(dict2.keys()) != set(dict1.keys()):
            return False
        
        word1_values = sorted(dict1.values())
        word2_values = sorted(dict2.values())
        return (set(word1_values) == set(word2_values)) and (word1_values == word2_values)
        
        
        return True


s = Solution()
# print(s.closeStrings("abc", "bca"))
# print(s.closeStrings("cabbba", "abbccc"))
# print(s.closeStrings("a", "aa"))
print(s.closeStrings("aabbzzc", "abbczzz"))

"""
c bbb aa -> ccc bb a

aa bb zz c
a bb c zzz

aa zz
a zzz
"""
