# Intuition
# The problem requires finding the length of the longest common subsequence between two given strings.
# A dynamic programming approach is suitable for solving this problem, where the goal is to build a 2D 
# array to store the lengths of common subsequences.

# Approach
# The provided code implements an optimized dynamic programming approach to find the length of the longest
# common subsequence. It uses a 1D array (`dp`) to store the lengths of common subsequences, 
# reducing space complexity to O(min(m, n)). The algorithm iterates through the characters of both strings, 
# updating the `dp` array based on whether the characters match or not.

# Complexity
# - Time complexity: O(m * n), where m and n are the lengths of the input strings.
# - Space complexity: O(min(m, n)), as the algorithm uses a 1D array of size n+1.

# Code
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # Use a 1D array to store the lengths of common subsequences
        dp = [0] * (n + 1)

        for i in range(1, m + 1):
            # Create a variable to store the value at the previous diagonal element
            prev_diag = 0

            for j in range(1, n + 1):
                # Store the current value in the dp array before updating it
                temp = dp[j]

                if text1[i - 1] == text2[j - 1]:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                # Update the prev_diag variable for the next iteration
                prev_diag = temp

        # The result is stored in the last element of the dp array
        return dp[n]
