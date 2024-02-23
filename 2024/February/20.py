# # Intuition
# The goal is to find the missing number in the given array. 
# The approach involves using the arithmetic sum formula to calculate the expected sum of all
#  numbers in the range [0, n]. By subtracting the sum of the given array from the expected sum,
#  the missing number can be identified.

# # Approach
# 1. Calculate the length of the array `n`.
# 2. Use the arithmetic sum formula to determine the expected sum of all numbers in the range [0, n].
# 3. Find the actual sum of the numbers in the given array.
# 4. Subtract the actual sum from the expected sum to obtain the missing number.
# 5. Return the missing number.

# # Complexity
# - Time complexity: O(n)
#   - The algorithm iterates over the array once to calculate the sum, and other operations are constant time.
# - Space complexity: O(1)
#   - The algorithm uses a constant amount of additional space.

# Code
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Arithmetic sum formula
        actual_sum = sum(nums)
        return expected_sum - actual_sum