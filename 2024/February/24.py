# # Intuition
# The given problem involves people having meetings at different times, where the secret is shared. 
# We want to determine the set of people who know the secret after all meetings. 
# The approach involves using a priority queue (min heap) to process meetings in chronological order, 
# keeping track of known people.

# # Approach
# - Build an adjacency list (`adj`) to represent the meetings.
# - Use a min heap (`pq`) to keep track of the meetings to be processed, prioritized by time.
# - Initialize `known` list to track the time each person becomes known.
# - Iterate through the meetings, pop from the heap, update the known people, and push new meetings.
# - Continue until the heap is empty.

# # Complexity
# - Time complexity: O(E * log(E)), where E is the number of edges (meetings).
# - Space complexity: O(E), where E is the number of edges (meetings).

# Code
import heapq

class Solution:
    def findAllPeople(self, n, meetings, firstPerson):
        adj = [[] for _ in range(n)]

        # Build adjacent lists
        for meet in meetings:
            x, y, time = meet
            adj[x].append((time, y))
            adj[y].append((time, x))

        known = [float('inf')] * n
        result = []
        pq = [(0, 0), (0, firstPerson)]  # min heap
        heapq.heapify(pq)

        while pq:
            s, x = heapq.heappop(pq)a

            if known[x] != float('inf'):
                continue

            result.append(x)
            known[x] = s

            for t, y in adj[x]:
                if known[y] != float('inf') or t < s:
                    continue

                heapq.heappush(pq, (t, y))

        return result