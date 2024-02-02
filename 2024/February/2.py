# # Intuition
# The problem requires generating sequential digits within a given range. The initial approach involves using a sliding window to create substrings of varying lengths, converting them to integers, and checking if they fall within the specified range.

# # Approach
# 1. Define a string of digits from "1" to "9" as `digits`.
# 2. Determine the length of the low and high values.
# 3. Iterate over lengths ranging from the length of `low` to the length of `high`.
# 4. For each length, iterate over possible starting indices (up to `10 - length`) and extract the corresponding substring from `digits`.
# 5. Convert the substring to an integer and check if it falls within the given range (`low` to `high` inclusive).
# 6. If the condition is met, append the integer to the result list.
# 7. Return the sorted result list.

# # Complexity
# - Time complexity: $$O(n)$$, where $$n$$ is the difference between the length of `high` and the length of `low`. The nested loops iterate over possible lengths and starting indices within the digit string.
# - Space complexity: $$O(1)$$, as the algorithm uses a constant amount of space for variables, and the result list is the only data structure that grows with the input size.

# # Code

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"

        low_length, high_length = len(str(low)), len(str(high))

        for length in range(low_length, high_length + 1):
            for i in range(10 - length):
                num_str = digits[i:i + length]
                num = int(num_str)
                if low <= num <= high:
                    result.append(num)

        return result