from collections import Counter, defaultdict
from types import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # My solution - O(n^2)으로 시간 복잡도 초과

        # answers = []
        # used = [0] * len(strs)
        # for i in range(len(strs)):
        #     if used[i]:
        #         continue
        #     dic = Counter(strs[i])
        #     same_word = [strs[i]]
        #     used[i] = 1
        #     for j in range(i+1, len(strs)):
        #         temp = Counter(strs[j])
        #         if dic == temp:
        #             same_word.append(strs[j])
        #             used[j] = 1

        #     answers.append(same_word)
        # return answers

        # Book Solution - 정렬을 통해 시간복잡도 O(n)으로 풀이 가능
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return list(anagrams.values())