# # Intuition
# The goal is to determine the minimum length of the string after applying a specific operation repeatedly. 
# The operation involves removing non-overlapping prefixes and suffixes with equal characters.

# # Approach
# I have used a two-pointer approach to find non-overlapping prefixes and suffixes with equal characters. 
# The pointers, `left` and `right`, start from the ends of the string and move towards the center. 
# If the characters at the `left` and `right` pointers are equal, I find the consecutive characters with the same
# value on both sides and move the pointers accordingly. This process continues until there are no more 
# non-overlapping prefixes and suffixes with equal characters.

# # Complexity
# - Time complexity: $$O(n)$$, where $$n$$ is the length of the input string. The two-pointer approach iterates 
# through the string once.
# - Space complexity: $$O(1)$$, as only two pointers (`left` and `right`) and a constant number of variables 
# are used. No additional data structures are employed.

# Code

class Solution {
    public int minimumLength(String s) {
        int left = 0, right = s.length() - 1;

        while (left < right && s.charAt(left) == s.charAt(right)) {
            char currentChar = s.charAt(left);
            while (left <= right && s.charAt(left) == currentChar) {
                left++;
            }
            while (left <= right && s.charAt(right) == currentChar) {
                right--;
            }
        }

        return right - left + 1;
    }
}
