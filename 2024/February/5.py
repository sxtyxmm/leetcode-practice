# # Intuition
# The problem involves finding the index of the first unique character in a given string. The provided solution appears to use two dictionaries, `char_count` and `char_index`, to keep track of character counts and the index of their first occurrence, respectively.

# # Approach
# The algorithm takes a single pass through the input string, updating the counts and indices in the dictionaries. After populating the dictionaries, it iterates through `char_count` to find the first character with a count of 1 and returns its index from `char_index`. If no unique character is found, it returns -1.

# # Complexity
# - Time complexity: $$O(n)$$, where n is the length of the input string. The algorithm performs a single pass through the string.
# - Space complexity: $$O(n)$$, where n is the length of the input string. The algorithm uses two dictionaries to store character counts and indices.

# Code

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}  # Dictionary to store character counts
        char_index = {}  # Dictionary to store the index of the first occurrence

        # Single pass: Populate char_count and char_index
        for i, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            char_index[char] = i if char not in char_index else char_index[char]

        # Find the first character with count 1 and return its index
        for char, count in char_count.items():
            if count == 1:
                return char_index[char]

        return -1  # Return -1 if no unique character is found
