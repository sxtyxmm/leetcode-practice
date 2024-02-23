# # Intuition
# The goal is to determine whether the given integer `n` is a power of two. A power of two has a binary representation
#  with only one bit set. 

# # Approach
# The provided code checks if `n` is positive and whether exactly one bit is set using the bitwise AND operation 
# `(n & (n - 1)) == 0`. The condition `n > 0` ensures that the number is positive.

# # Complexity
# - Time complexity: O(1)
#   - The bitwise AND operation and comparisons take constant time regardless of the value of `n`.
# - Space complexity: O(1)
#   - The algorithm uses a constant amount of additional space.

# Code
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is positive and exactly one bit is set
        return n > 0 and (n & (n - 1)) == 0