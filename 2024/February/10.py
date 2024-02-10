# ## Intuition
# The given code appears to implement a solution to count the number of palindromic substrings in a given string `s`.
# The approach seems to involve expanding around each character and checking for palindromes with odd and even lengths.

# ## Approach
# The `countSubstrings` method iterates through each character in the string `s`. For each character, it calls the 
# `expand_around_center` function twice – once with the current character as the center for odd-length palindromes, 
# and once with the current character and the next character as the center for even-length palindromes. 
# The `expand_around_center` function is responsible for expanding the palindrome around the center and updating the count.

# ## Complexity
# - Time complexity: $$O(n^2)$$
#   - The nested loop iterates through each character in the string, and for each character, it may expand to both sides,
#     resulting in a quadratic time complexity.
# - Space complexity: $$O(1)$$
#   - The algorithm uses a constant amount of extra space, and the space complexity is not dependent on the input size.

## Code

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        def expand_around_center(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        for i in range(n):
            expand_around_center(i, i)  
            expand_around_center(i, i + 1)  
        return count