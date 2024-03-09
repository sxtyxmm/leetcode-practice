# # Intuition
# The goal is to find the total frequencies of elements in the given array such that those elements have the maximum 
# frequency.

# # Approach
# I have used the following approach to solve the problem:
# 1. Count the frequency of each element in the array using the `Counter` class from the `collections` module.
# 2. Find the maximum frequency among all elements.
# 3. Sum up the frequencies of elements that have the maximum frequency.

# # Complexity
# - Time complexity: $$O(n)$$, where $$n$$ is the length of the input array. 
# Counting the frequency of elements using the `Counter` class takes linear time.
# - Space complexity: $$O(n)$$, as additional space is required to store the frequency 
# counts in the `freq_counter` dictionary. The space complexity is linear with respect 
# to the size of the input array.

# Code

from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Step 1: Count the frequency of each element
        freq_counter = Counter(nums)
        
        # Step 2: Find the maximum frequency
        max_frequency = max(freq_counter.values())
        
        # Step 3: Sum up frequencies of elements with the maximum frequency
        total_frequency = sum(freq for freq in freq_counter.values() if freq == max_frequency)
        
        return total_frequency