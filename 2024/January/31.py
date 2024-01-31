# Intuition
## The intuition behind this solution is to use a stack to keep track of the indices of the temperatures.
## We iterate through the given temperatures, and for each temperature, we check if it is greater than the 
## temperature at the index stored at the top of the stack. If it is, we update the result for that index by
## calculating the difference between the current index and the popped index from the stack. 
## This represents the number of days until a warmer temperature.

# Approach
## 1. Initialize a deque (double-ended queue) called `stack` to store the indices of temperatures.
## 2. Initialize a list called `result` with zeros, representing the output for each day.
## 3. Iterate through the given temperatures using the enumerate function to get both the index and temperature.
## 4. Inside the loop, check if the stack is not empty and the current temperature is greater than the temperature
## at the index stored at the top of the stack.
## 5. If the condition is met, pop the index from the stack and update the result for that index by calculating 
##the difference between the current index and the popped index.
## 6. Append the current index to the stack.
## 7. After the loop, return the `result` list.

# Complexity
## - Time complexity: O(n), where n is the number of temperatures. Each index is pushed and popped from the stack at most once.
## - Space complexity: O(n), where n is the number of temperatures. 
## The space used by the stack and result list is proportional to the number of temperatures.

# Code

from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result
