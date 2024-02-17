# # Intuition
# The provided code seems to be aimed at finding the largest perimeter of a triangle given an array of side lengths.
# The intuition behind the approach is to sort the array and then iterate through it, checking for valid triangles
# by comparing the current element with the sum of the previous two elements.

# # Approach
# 1. Sort the input array `nums` in ascending order.
# 2. Initialize variables `sum_val` and `ans` to keep track of the sum of two smaller sides and the potential
# largest perimeter, respectively.
# 3. Iterate through the sorted array, updating `sum_val` and checking if the current element can form a valid
# triangle with the two preceding elements.
# 4. Update `ans` if a valid triangle is found.
# 5. Return the final result stored in `ans`.

# # Complexity
# - Time complexity: The time complexity is dominated by the sorting step, which is typically $$O(n \log n)$$ 
#for Python's built-in sorting algorithm, where $$n$$ is the length of the input array.
# - Space complexity: The space complexity is $$O(1)$$ as the algorithm uses a constant amount of additional space.

# Code
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans