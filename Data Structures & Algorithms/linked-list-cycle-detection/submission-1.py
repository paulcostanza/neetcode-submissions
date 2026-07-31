# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # goes up by 1
        # goes up by 2
        # if goes up by 2 is None, there is no cycle
        # if they meet, there is a cycle

        one_step = head
        two_step = head

        while one_step and one_step.next and two_step and two_step.next and two_step.next.next:
            one_step = one_step.next
            two_step = two_step.next.next

            if one_step == two_step:
                return True


        return False
        