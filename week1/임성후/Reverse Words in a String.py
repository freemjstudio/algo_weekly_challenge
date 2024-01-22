class Solution(object):
    def reverseWords(self, s: str):
        splitted = s.split(" ")
        result = []
        for split in splitted:
            if split == "":
                continue
            result.append(split)
        answer = []
        for rev in result[::-1]:
            answer.append(rev)
        return " ".join(answer)
        



