# ## Intuition
# The intuition for this solution is to use the `Counter` class from the `collections` module to count the
# frequency of each character in the input string. Then, the characters are sorted based on their frequency
# in descending order. Finally, a sorted string is constructed by repeating each character according to its frequency.

# ## Approach
# The approach involves using the `Counter` class to count character frequencies and then sorting the characters
# based on their frequencies in descending order. The sorted characters are then joined to create the final sorted string.

# ## Complexity
# - Time complexity: The time complexity is dominated by the sorting step, which is O(n log n),
# where n is the length of the input string.
# - Space complexity: The space complexity is O(n), where n is the length of the input string. 
# This is due to the space required to store the character frequencies in the Counter.

# Code

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequency = Counter(s)
        sorted_string = ''.join(char * freq for char, freq in sorted(char_frequency.items(), key=lambda x: x[1], reverse=True))
        return sorted_string