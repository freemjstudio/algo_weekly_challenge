# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150

import heapq
import heapq

# 첫번째 시도
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        result = []

        for i in nums1:
            for j in nums2:
                heapq.heappush(result, [(i + j), i, j])

        answer = []
        for _ in range(k):
            temp = heapq.heappop(result)
            answer.append(temp[1:])

        return answer

# 두번쨰 시도
import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        queue = []
        # heapq 에 모든 pair 를 집어넣지 않아도 됨
        for i in range(min(len(nums1), k)):
            heapq.heappush(queue, ((nums1[i] + nums2[0], i, 0)))

        answer = []
        while len(answer) < k and queue:
            s, i, j = heapq.heappop(queue)
            answer.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(queue, ((nums1[i] + nums2[j + 1]), i, j + 1))
        return answer
