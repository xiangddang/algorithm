#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        cur = head
        while cur.next:
            count += 1
            cur = cur.next
        if count == n:
            return head.next
        cur = head
        for i in range(count - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head
        
# @lc code=end

