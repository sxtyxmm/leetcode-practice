# # Intuition
# To solve this problem efficiently, we can utilize the concept of prefix and suffix products. 
# By calculating the prefix products and suffix products of the given array, we can then multiply
# the corresponding prefix and suffix products to obtain the final result. 

# # Approach
# We iterate through the array twice: first to calculate the prefix products and then to calculate the suffix products. 
# For each index, we store the prefix product up to that index. Then, we traverse the array backward to calculate the 
# suffix products. Finally, we multiply the prefix and suffix products (excluding the current element) to obtain the 
# desired product except self.

# # Complexity
# - Time complexity: O(n), where n is the length of the input array. We iterate through the array twice, 
# each time with a linear time complexity operation.
# - Space complexity: O(n), where n is the length of the input array. We use additional space to store the answer array.

# Code

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate suffix products and multiply with prefix products to get the final answer
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix_product
            suffix_product *= nums[i]

        return answer