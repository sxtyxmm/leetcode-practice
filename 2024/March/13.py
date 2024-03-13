class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2  # Formula to calculate the sum of integers from 1 to n

        current_sum = 0
        for x in range(1, n + 1):
            remaining_sum = total_sum - current_sum - x

            if remaining_sum == current_sum:
                return x

            current_sum += x

        return -1
