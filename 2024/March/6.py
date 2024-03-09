# # Intuition
# The task is to determine whether a linked list contains a cycle. My initial thought is to use the slow
# and fast pointer approach to detect a cycle in the linked list.

# # Approach
# I have implemented the solution using two pointers, `slowPointer` and `fastPointer`. The `slowPointer` 
# advances one step at a time, while the `fastPointer` advances two steps at a time. If there is a cycle, 
# the two pointers will eventually meet. If there is no cycle, the `fastPointer` will reach the end of the list.

# # Complexity
# - Time complexity: $$O(n)$$, where $$n$$ is the number of nodes in the linked list. The slow pointer will
#  traverse the list once, and the fast pointer, in the worst case, will traverse it twice (if there is a cycle).
# - Space complexity: $$O(1)$$, as only two pointers (`slowPointer` and `fastPointer`) are used, and no
# additional data structures are employed. The space complexity is constant with respect to the size of the input 
# linked list.

# Code

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false;
        }

        ListNode slowPointer = head;
        ListNode fastPointer = head.next;

        while (slowPointer != fastPointer) {
            if (fastPointer == null || fastPointer.next == null) {
                return false; // If there is no cycle, fastPointer will reach the end of the list
            }
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
        }

        return true; // If there is a cycle, slowPointer and fastPointer will meet
    }
}
