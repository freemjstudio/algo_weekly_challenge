from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        num_dict = defaultdict(list)
        result = []
        for i, v in enumerate(groupSizes):
            num_dict[v].append(i)
            if v == len(num_dict[v]):
                result.append(num_dict[v])
                num_dict[v] = []
        return result


s = Solution()
print(s.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(s.groupThePeople([2, 1, 3, 3, 3, 2]))
