# # Intuition
# The goal is to permute the characters of string `s` according to the custom order specified in string `order`. 
# To achieve this, we can count the occurrences of each character in `s` using a dictionary. Then, we iterate 
# through the custom order and append the characters to the result string based on their occurrences in `s`. 
# Finally, we add the remaining characters from `s` to the end of the result string.

# # Approach
# 1. Initialize a dictionary `char_count` to store the count of each character in `s`.
# 2. Iterate through string `s` and update the counts in the `char_count` dictionary.
# 3. Initialize an empty list `result` to store the characters in the desired order.
# 4. Iterate through the characters in the custom order (`order`).
#    - If the character is present in the `char_count` dictionary, append it to the result string multiplied 
#      by its count and remove it from the dictionary.
# 5. Append the remaining characters from `char_count` to the end of the result string.
# 6. Return the concatenated result string.

# # Complexity
# - Time complexity: O(n), where n is the length of string `s`.
# - Space complexity: O(n), as the `char_count` dictionary stores the counts of characters in `s`.

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        result = []
        for char in order:
            if char in char_count:
                result.append(char * char_count[char])
                del char_count[char]
        for char in char_count:
            result.append(char * char_count[char])
        return ''.join(result)