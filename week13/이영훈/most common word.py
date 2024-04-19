from types import List 
from collections import Counter
import re 

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        arr = []
        for word in paragraph.split(','):
            temp = re.sub(r'[^a-zA-Z\s]', '', word)
            for w in temp.split():
                w = w.lower()
                if w not in banned:
                    arr.append(w)

        counter = Counter(arr)
        counter_list = [(k, v) for k, v in counter.items()]
        counter_list.sort(key = lambda x : -x[1])
        return counter_list[0][0]