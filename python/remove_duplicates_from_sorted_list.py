# ======================================
# LeetCode Problem: remove duplicates from sorted list
# Language: python3
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Synced by: LinkCode
# Date: 2026. 6. 2. 오전 3:32:31
# ======================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        vals = []
        while prev is not None:
            if len(vals) == 0:
                vals.append(prev.val)
                continue
            if vals and vals[-1] != prev.val:
                vals.append(prev.val)
            prev = prev.next
        
        result = None
        temp = None
        for v in vals:
            print(v)
            if result is None:
                result = ListNode(v, None)
                temp = result
            else:
                temp.next = ListNode(v, None)
                temp = temp.next
                
        return result
