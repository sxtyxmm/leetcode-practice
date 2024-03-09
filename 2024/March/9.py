# # Intuition
# The goal is to find the minimum common integer between two sorted arrays.

# # Approach
# I have used a two-pointer approach to iterate through both sorted arrays simultaneously. 
# The pointers `i` and `j` are initialized to the start of the arrays. While iterating, 
# I compare the elements at the current positions. If they are equal, I return the common integer.
#  If the element in the first array (`nums1[i]`) is smaller, I increment the pointer `i`, and if 
# the element in the second array (`nums2[j]`) is smaller, I increment the pointer `j`. This process 
# continues until a common integer is found or one of the arrays is exhausted.

# If no common integer is found, I return -1.

# # Complexity
# - Time complexity: $$O(n)$$, where $$n$$ is the minimum length of the two input arrays. 
# In the worst case, we may need to iterate through both arrays entirely.
# - Space complexity: $$O(1)$$, as no additional space is used beyond the input arrays and 
# a constant number of variables.

# Code

from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return -1