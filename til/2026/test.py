''' Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

before solve this problem, I took a quick review on dictionary in python, where we can use key-value pairs to store data.This way can help us to map opening bracket to the closeing bracket easily.

'''

# Solution 
class Solution(object):
    def isValid(self, s): 
        """
        :type s: str
        :rtype: bool
        """
        stack = [] 
        mapping = {")": "(", "}": "{", "]": "["}  # These keys and values are paired brackets

        # now we create a loop to iterate through each character in the string s
        for char in s:
            # if the character is one of the closing brackets
            if char in mapping:
                # we pop the topmost element from the stack if it is non-empty, otherwise assign a dummy value of '#'
                top_element = stack.pop() if stack else '#'

                # the mapping for the closing bracket in the string must match the top element of the stack
                if mapping[char] != top_element:
                    return False
            else:
                # we push the opening bracket onto the stack
                stack.append(char)
        # if the stack is empty, then we have a valid expression
        return not stack