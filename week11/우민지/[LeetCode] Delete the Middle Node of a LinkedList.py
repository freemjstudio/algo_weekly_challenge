# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_val = []

        nodes_val.append(head.val)
        # 전체 linked list 를 순회함
        node = head
        while True:
            node = node.next
            if node == None:
                break
            else:
                nodes_val.append(node.val)

        # 중간 값을 index 로 삭제하기
        if len(nodes_val) <= 1:
            return None

        mid = len(nodes_val) // 2
        nodes_val.pop(mid)

        node = head
        front = ListNode()
        for i in range(mid):
            if i == mid - 1:
                front = node
            node = node.next
        back = node.next
        front.next = back

        return head