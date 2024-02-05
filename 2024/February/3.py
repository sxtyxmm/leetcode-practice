#  # Intuition
# The problem appears to involve maximizing the sum of non-overlapping subarrays in a given array 
# with a constraint on the maximum subarray length. The dynamic programming approach seems appropriate for this scenario.

# # Approach
# The provided code implements a dynamic programming solution. It iterates through the array, calculating the maximum sum
# for each position based on the previous results. The inner loop considers subarrays of different lengths up to the specified constraint 'k'. 
# The maximum sum for each position is updated using the optimal solution from the previous subarray lengths.

# # Complexity
# - Time complexity: $$O(nk)$$, where 'n' is the length of the array and 'k' is the specified constraint.
# - Space complexity: $$O(n)$$, as the algorithm uses an array of size 'n' for dynamic programming.

# The time complexity is influenced by the nested loop, iterating through the array and considering subarrays up to length 'k'. 
# The space complexity is determined by the array 'dp' used for dynamic programming.

# Code

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            curr_max = 0
            for j in range(1, min(k, i + 1) + 1):
                curr_max = max(curr_max, arr[i - j + 1])
                dp[i] = max(dp[i], (dp[i - j] if i - j >= 0 else 0) + curr_max * j)

        return dp[-1]
