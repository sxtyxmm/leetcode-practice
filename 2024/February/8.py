## Intuition
#The problem appears to be focused on finding the minimum number of perfect square numbers that sum up to a given 
#integer 'n'. The dynamic programming approach is evident from the use of a 1D array (dp) to store intermediate results. 

# # Approach
# The provided solution employs dynamic programming to iteratively build the minimum number of perfect squares
# needed to reach each number up to 'n'. The outer loop iterates through numbers from 1 to 'n', and the inner 
# loop considers all possible perfect square numbers less than or equal to the current number. The minimum count
# of perfect squares needed to reach the current number is updated in the dp array.

# # Complexity
# - Time complexity: $$O(n \sqrt{n})$$
#   - The outer loop runs in O(n) time, and the inner loop iterates up to $$\sqrt{n}$$.
# - Space complexity: $$O(n)$$
#   - The dp array requires O(n) space.

# Code

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]