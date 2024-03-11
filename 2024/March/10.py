from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the intersection of the two sets
        result = list(set1.intersection(set2))

        return result

# Example usage:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]
solution_instance = Solution()
result = solution_instance.intersection(nums1, nums2)
print(result)
