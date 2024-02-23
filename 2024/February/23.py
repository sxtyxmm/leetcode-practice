# # Intuition
# The problem seems to involve finding the cheapest price to reach the destination within a certain number of stops.
#  The given code utilizes BFS (Breadth-First Search) to explore possible paths with a limited number of stops and updates the minimum cost to reach each node.

# # Approach
# The code initializes an adjacency list to represent the graph and uses a deque to perform BFS. 
# The distance array keeps track of the minimum cost to reach each node. The algorithm iteratively explores nodes, updating the distance array with the minimum cost for reaching each node within the specified number of stops.

# # Complexity
# - Time complexity: The time complexity is dependent on the number of nodes and edges in the graph and the
#  maximum number of stops allowed. In the worst case, where all nodes are explored, the time complexity is O(n * k),
# where n is the number of nodes and k is the maximum number of stops allowed.
  
# - Space complexity: The space complexity is determined by the adjacency list and the distance array.
# In the worst case, the space complexity is O(n), where n is the number of nodes.

# Code
from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        q = deque([(src, 0, 0)])  # Tuple: (node, stops, distance)

        while q:
            node, stops, distance = q.popleft()

            if stops > k:
                continue

            for neighbour, price in adj[node]:
                if price + distance >= dist[neighbour]:
                    continue

                dist[neighbour] = price + distance
                q.append((neighbour, stops + 1, dist[neighbour]))

        return dist[dst] if dist[dst] != INF else -1