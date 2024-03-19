# # Intuition
# To solve this problem, we need to find the minimum number of intervals required to complete all tasks while 
## respecting the cooling time constraint. Our goal is to optimize the scheduling of tasks to minimize the total 
# number of intervals.

# # Approach
# We approach this problem by first identifying the tasks with the maximum frequency. These tasks need to be spaced 
# out by at least `n` intervals. We calculate the intervals required for these tasks based on the maximum frequency 
# and the cooling time.

# We also count the number of tasks that have the same maximum frequency. These tasks, along with their cooldown periods,
# contribute to the overall intervals required.

# Finally, we return the maximum of the intervals calculated above and the total number of tasks.

# # Complexity
# - Time complexity:  
#   - Sorting the task frequencies takes O(n log n) time, where n is the number of unique tasks.
#   - Calculating the intervals takes O(1) time.
#   - Counting the number of tasks with the same maximum frequency takes O(n) time.
#   - Overall time complexity is O(n log n).

# - Space complexity:
#   - We use a counter to store the frequency of each task, which requires O(n) space.
#   - Other variables and operations require O(1) space.
#   - Overall space complexity is O(n).

# Code

from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_freq = Counter(tasks)
        max_freq = max(task_freq.values())
        max_freq_tasks_count = sum(1 for freq in task_freq.values() if freq == max_freq)
        intervals = (max_freq - 1) * (n + 1) + max_freq_tasks_count
        return max(intervals, len(tasks))