# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Create an array
        # loop through the link list
        # add each node to the array
        # reverse the array
        # re-construct the link list

        nodes = []
        
        curr = head
        while curr:
            next_node = curr.next
            curr.next = None
            nodes.append(curr)
            curr = next_node

        if len(nodes) > 0:
            for node_index in range(len(nodes) - 1, 0, -1):
                nodes[node_index].next = nodes[node_index - 1]
            return nodes[len(nodes) - 1]
        else:
            return None