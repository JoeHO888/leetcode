# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # In place reverse
        # prev -> None
        # curr -> Head
        # next_ -> Head.next

        # o -> o -> o -> o
        # current is 2nd o
        # whenever curr is not none
        # next = curr.next # keep next node
        # 3rd o
        # link curr to  prev
        # o <- o  o -> o
        # move prev to current o we are considering (2nd o)
        # move curr to original old o, i.e. 3rd o
        
        # Finally, when move to last node
        # prev will be the current o we are considering o, i.e. the last node
        # so return the prev

        prev = None
        curr = head

        while curr:
            next_ = curr.next
            curr.next = prev
            prev, curr = curr, next_
        return prev