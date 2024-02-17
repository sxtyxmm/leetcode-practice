# # Intuition
# The problem revolves around efficiently traversing a series of buildings while optimizing the use of bricks
# and ladders to reach the furthest building possible. The primary consideration is to use ladders for the tallest
# buildings with the largest height differences, allowing for greater flexibility.

# # Approach
# The algorithm uses a priority queue (min heap `diff_heap`) to store the differences in heights between consecutive
# buildings. This allows for efficient retrieval of the smallest height differences. The algorithm iterates through
# the buildings, calculating the height differences and using ladders or bricks as needed.

# The key strategy involves prioritizing the largest height differences by using a priority queue. If the number
# of differences exceeds the available ladders, bricks are used instead of the ladder with the smallest difference.
# If bricks become insufficient, the algorithm returns the index of the last successfully traversed building.

# # Complexity
# - Time complexity: O(n log k), where n is the length of the `heights` array, and k is the minimum of `ladders`
# and the number of positive differences between consecutive buildings. The dominant factor is the heap operations
# (insertion and removal) within the loop.
# - Space complexity: O(k), where k is the minimum of `ladders` and the number of positive differences between
# consecutive buildings. The space complexity is determined by the size of the `diff_heap`.

# Code

from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        diff_heap = []  # Min heap to store the differences in heights

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(diff_heap, diff)

                # If the number of differences exceeds the number of ladders available,
                # use bricks instead of the ladder with the smallest difference
                if len(diff_heap) > ladders:
                    bricks -= heapq.heappop(diff_heap)

                # If bricks are negative, we cannot move further
                if bricks < 0:
                    return i

        # If we reach here, it means we can reach the last building
        return n - 1