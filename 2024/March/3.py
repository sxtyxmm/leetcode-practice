# # Intuition
# The problem involves removing the nth node from the end of a linked list. To achieve this efficiently,
#  we can use a two-pointer approach. By maintaining a gap of n+1 between the fast and slow pointers, we
#  can easily identify the node to be removed.

# # Approach
# 1. Initialize two pointers, `fast` and `slow`, both starting at a dummy node.
# 2. Move the `fast` pointer n+1 steps ahead to create the desired gap.
# 3. Move both pointers simultaneously until the `fast` pointer reaches the end of the list.
# 4. The `slow` pointer will be at the node just before the one to be removed.
# 5. Adjust the pointers to remove the nth node from the end.

# # Complexity
# - Time complexity: O(N) - The algorithm traverses the linked list once.
# - Space complexity: O(1) - Constant space is used as only a fixed number of pointers are maintained.

# Code

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers: fast and slow
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next