# Intuition
# The goal is to divide the given array into subarrays of at most three elements,
#  where the difference between the maximum and minimum element in each subarray is at most `k`.
#  This problem can be approached by sorting the array and then greedily forming subarrays.

# Approach
# 1. Sort the given array `nums` in ascending order.
# 2. Initialize an empty list `result` to store the subarrays that meet the criteria.
# 3. Initialize an index `i` to traverse the sorted array.
# 4. While traversing the array, take subarrays of at most three elements starting from the current index `i`.
# 5. Check if the difference between the maximum and minimum element in the subarray is at most `k`.
# 6. If it is, add the subarray to the `result` list and move to the next non-overlapping subarray.
# 7. If not, return an empty list, as it is not possible to satisfy the criteria.

## Complexity
# - Time complexity: O(n log n) due to the sorting operation.
# - Space complexity: O(n) for the `result` list to store the subarrays.

# Code

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        i = 0
        while i < n:
            subarray = nums[i:i+3]
            if subarray[-1] - subarray[0] <= k:
                result.append(subarray)
                i += 3
            else:
                return []

        return result