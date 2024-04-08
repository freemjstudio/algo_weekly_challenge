from types import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def bfs(index, path):
            if len(digits) == len(path):
                result.append(path)
                return 

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    bfs(i+1, path+j)
        
        result = []
        dic = {
            '2' : "abc",
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
            }

        if len(digits) == 0:
            return []
            
        bfs(0, "")
        return result