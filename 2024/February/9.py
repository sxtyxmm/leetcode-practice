# ## Intuition
# The problem involves finding the largest divisible subset from a given list of integers. 
# The initial intuition is to sort the array and use dynamic programming to keep track of the divisible subsets.

# ## Approach
# The provided code implements a solution using dynamic programming. It first sorts the input array, 
# then iterates through the sorted array, maintaining a dynamic programming array (`dp`) to store the 
# size of the largest divisible subset ending at each index. Additionally, a `parent` array is used to 
# keep track of the previous index contributing to the current subset. The algorithm identifies the maximum 
# size and corresponding index of the largest divisible subset.

# ## Complexity
# - Time complexity: $$O(n^2)$$, where \(n\) is the length of the input array. The nested loops iterate 
# through the array and perform constant time operations.
# - Space complexity: $$O(n)$$, as additional space is used for the `dp` and `parent` arrays, both of size \(n\).

## Code

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n  
        parent = [-1] * n  
        max_size, max_index = 1, 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        return result[::-1]