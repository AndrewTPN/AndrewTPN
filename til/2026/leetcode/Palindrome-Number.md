# Palindrome Number (Easy)
# Date: Jan 16, 2026
#
# Problem:
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1: Input: x = 121  -> Output: true
# Example 2: Input: x = -121 -> Output: false
# Example 3: Input: x = 10   -> Output: false
#
# Solution guide:
# Reverse the number and compare. Negative numbers are not palindromes.
# Use string slicing [::-1] to reverse, then compare with original.

# create the function
def isPalindrome(self, x):
    # negative numbers are not palindrome
    if x < 0:
        return False
    
    # convert number to string and reverse it
    reversed_x = str(x)[::-1]
    
    # compare original number with reversed number
    return str(x) == reversed_x

# test the function
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
