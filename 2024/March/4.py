# # Intuition
# The task is to maximize the total score by strategically playing tokens. The two possible moves are playing a 
# token face-up or face-down. To maximize the score, we need to make optimal choices based on the current power and score.

# # Approach
# I have used a two-pointer approach after sorting the tokens. The `left` pointer starts from the beginning of the
# sorted list, and the `right` pointer starts from the end. The while loop continues until the pointers meet. If the
#  current power is enough to play a token face-up, we play it face-up and increment the `left` pointer and the score. 
# If the score is greater than 0, we can play a token face-down, increment the `right` pointer, and decrement the score.
#  We keep track of the maximum score achieved during the process.

# # Complexity
# - Time complexity: $$O(n \log n)$$, where $$n$$ is the number of tokens. 
# The sorting step takes $$O(n \log n)$$ time, and the subsequent two-pointer traversal is linear.
# - Space complexity: $$O(1)$$, as only a constant number of variables (`left`, `right`, `score`, `max_score`) are used.
#  No additional data structures are employed.

# Code

from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score