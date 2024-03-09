# # Intuition
# The goal is to find the middle node of a singly-linked list. The idea is to use the slow and fast pointer approach
#  to traverse the list and locate the middle node.

# # Approach
# I have used two pointers, `slowPointer` and `fastPointer`, initially pointing to the head of the linked list. 
# The `slowPointer` advances one step at a time, while the `fastPointer` advances two steps at a time. 
# This way, when the `fastPointer` reaches the end of the list, the `slowPointer` will be at the middle node.

# # Complexity
# - Time complexity: $$O(n)$$, where $$n$$ is the number of nodes in the linked list. Both pointers traverse 
# the list, and in the worst case, the `fastPointer` reaches the end after $$n/2$$ iterations.
# - Space complexity: $$O(1)$$, as only two pointers (`slowPointer` and `fastPointer`) are used, and no 
# additional data structures are employed. The space complexity is constant with respect to the size of the 
# input linked list.

# Code

class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slowPointer = head;
        ListNode fastPointer = head;

        while (fastPointer != null && fastPointer.next != null) {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
        }

        return slowPointer;
    }
}
