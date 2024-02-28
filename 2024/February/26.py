# # Intuition
# The intuition behind this approach is to recursively compare the nodes and their respective subtrees in the binary trees
# `p` and `q`. The function checks whether the current nodes are equal and then proceeds to check their left and right 
#subtrees.

# # Approach
# 1. Define the `TreeNode` class to represent the structure of a binary tree node.
# 2. Implement the `isSameTree` method within the `Solution` class.
# 3. Use a recursive approach to compare the nodes and their subtrees.
# 4. Base case: If both nodes are `None`, return `True` (indicating equality).
# 5. If one of the nodes is `None` or their values are different, return `False` (indicating inequality).
# 6. Recursively check the left and right subtrees.
# 7. Example usage demonstrates creating an instance of the `Solution` class, initializing two binary trees 
#(`p` and `q`), and calling the `isSameTree` method to check if they are the same.

# # Complexity
# - Time complexity: O(n), where n is the total number of nodes in the binary trees. The function needs to visit
# each node once.
# - Space complexity: O(h), where h is the height of the binary trees. This represents the maximum depth of the
# recursive call stack. In the worst case, when the trees are skewed, the space complexity is O(n).

# Code

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: If both nodes are None, they are equal
        if not p and not q:
            return True

        # If one of the nodes is None or their values are different, they are not equal
        if not p or not q or p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
solution = Solution()

p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))

result = solution.isSameTree(p, q)
print(result)