# # Intuition
# The problem requires finding the leftmost value in the last row of a binary tree. To achieve this, a level-order 
# traversal approach is employed. The idea is to traverse the tree level by level, and at each level, record the 
# leftmost value. The final recorded leftmost value corresponds to the leftmost node in the last row.

# # Approach
# The approach involves using a queue to perform a level-order traversal of the binary tree. Starting from the root, 
# each level's nodes are processed, and their child nodes are added to the queue for subsequent levels. The leftmost 
# value at each level is updated during the traversal. The final leftmost value recorded corresponds to the desired result.

# # Complexity
# - Time complexity: O(n), where n is the number of nodes in the binary tree. Each node is visited once during the 
# level-order traversal.
# - Space complexity: O(m), where m is the maximum number of nodes at any level in the binary tree. In the worst case, 
# the queue may store all nodes at a particular level.

# Code
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        queue = deque([root])
        while queue:
            level_size = len(queue)

            # Traverse all nodes at the current level
            for i in range(level_size):
                current_node = queue.popleft()

                # Add child nodes to the queue (right first, then left)
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)

            # The leftmost node value at the last level
            leftmost_value = current_node.val

        return leftmost_value