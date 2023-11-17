#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr = list(set(arr))
        arr.sort()
        dummy = ListNode()
        curr = dummy
        for i in arr:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
            
# @lc code=end

