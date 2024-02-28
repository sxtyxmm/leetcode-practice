# # Intuition
# The problem involves finding the diameter of a binary tree, which is defined as the length of the longest path between
# any two nodes in a tree. The path may or may not pass through the root. One way to approach this is to perform a 
# depth-first search (DFS) traversal of the tree while keeping track of the height of each subtree. The diameter can then
# be updated at each node by considering the sum of heights of its left and right subtrees.

# # Approach
# I have implemented a solution using a recursive DFS approach. The `diameterOfBinaryTree` function takes the root of the
# binary tree as input and uses a helper function `dfs` to perform the DFS traversal. The `dfs` function calculates the
# height of each subtree and updates the diameter accordingly. The final result is the diameter of the binary tree.

# # Complexity
# - Time complexity: O(n), where n is the number of nodes in the binary tree. The algorithm traverses each node once.
# - Space complexity: O(h), where h is the height of the binary tree. The space complexity is determined by the maximum 
#height of the recursive call stack.

# Code
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            
            # Recursively calculate the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update diameter by considering the path that passes through the current node
            diameter = max(diameter, left_height + right_height)
            
            # Return the height of the current subtree
            return 1 + max(left_height, right_height)
        
        diameter = 0
        dfs(root)
        return diameter