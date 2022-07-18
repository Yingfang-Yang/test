class ListNode:
    """链表数据结构"""
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 尾结点
        last = None
        while head:
            head.next, last, head = last, head, head.next
        return last