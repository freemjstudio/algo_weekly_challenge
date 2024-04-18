from types import List 

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        string_lists = []
        digit_lists = []
        results = []

        for log in logs:
            log_list = list(log.split())
            if log_list[1].isdigit():
                digit_lists.append(log)
            else:
                string_lists.append(log)
        

        string_lists.sort(key = lambda x : (list(x.split())[1:], list(x.split())[0]))
        
        return string_lists + digit_lists 