# # Intuition
# The intuition behind this solution is to use a greedy strategy to merge elements with a common factor, 
# ensuring connectivity between indices. The approach relies on sorting the elements in reverse order and
# using the `math.gcd` function to identify common factors.

# # Approach
# 1. If the length of the input array `nums` is 1, return True as there's only one element.
# 2. Convert `nums` to a set to eliminate duplicate values.
# 3. If the number 1 is in the set, return False as it cannot be traversed to any other index.
# 4. Sort the set `nums` in reverse order.
# 5. Iterate through the sorted set and for each element, try to find another element with a common
# factor using the `math.gcd` function.
# 6. If a common factor is found, multiply the two elements and break out of the inner loop.
# 7. If no common factor is found for an element, return False.
# 8. If the iteration completes without returning False, return True.

# # Complexity
# - Time complexity: O(n log n), where n is the number of unique elements in the input array. 
# The sorting step dominates the time complexity.
# - Space complexity: O(n), where n is the number of unique elements in the input array. 
# The set and sorted list are used to store and process unique elements.

# Code
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        
        nums = sorted(nums, reverse=True)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    nums[j] *= nums[i]
                    break
            else:
                return False
        return True