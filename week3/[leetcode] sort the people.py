class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        name_dict = {}
        for n, h in zip(names, heights):
            name_dict[h] = n
        return [name_dict[k] for k in sorted(name_dict.keys(), reverse=True)]


