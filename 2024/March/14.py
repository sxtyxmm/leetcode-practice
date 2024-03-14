# # Intuition
# To efficiently count the number of subarrays with a given sum (goal), we can utilize the prefix sum technique. 
# By maintaining a prefix sum and keeping track of its frequency, we can determine the number of subarrays with 
# the desired sum.

# # Approach
# The approach involves iterating through the array of integers (nums) and calculating the prefix sum at each position.
# We maintain a frequency array to store the count of each prefix sum encountered so far. For each prefix sum, we check
# if the difference between the current sum and the goal exists in the frequency array. If it does, we increment the count
# by the corresponding frequency value. Finally, we update the frequency array with the current prefix sum.

# # Complexity
# - Time complexity: O(n), where n is the length of the input array nums. The algorithm iterates through nums 
#  once to calculate the prefix sum and update the frequency array.
# - Space complexity: O(n), where n is the length of the input array nums. The algorithm requires additional 
# space to store the frequency array, which has a length of len(nums) + 1.

# Code

from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum_freq = [0] * (len(nums) + 1)
        current_sum = 0
        
        prefix_sum_freq[0] = 1  # Initialize with 1 to handle cases where current_sum - goal = 0
        
        for num in nums:
            current_sum += num
            if current_sum - goal >= 0:
                count += prefix_sum_freq[current_sum - goal]
            prefix_sum_freq[current_sum] += 1
        
        return count
