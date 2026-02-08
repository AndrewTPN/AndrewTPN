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
        mapping = {
                    ")": "(", 
                    "}": "{", 
                    "]": "["
                    }  # These keys and values are paired brackets

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
    


    'dictionary in python is  a collection of key-value pairs. Each key is unique and is used to store and retrieve values efficiently. Dictionaries are mutable, meaning they can be changed after their creation'
    # Example of dictionary
    capitals = {
        "USA": "Washington, D.C.",
        "France": "Paris",
        "Japan": "Tokyo",
        "Vietnam": "Hanoi"
    }

    # Accessing values using keys
    print(capitals["France"]) 

#List
' [] this is a list in python, which is an ordered collection of items that can be of different types. Lists are mutable, meaning you can change their content after creation by adding, removing, or modifying elements.'
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Output: banana
'() Stack, which is a data structure that follows the Last In First Out (LIFO) principle. You can add (push) and remove (pop) items from the top of the stack.'
'{} Set, which is an unordered collection of unique items. Sets are useful for membership testing and eliminating duplicate entries.'
# those parentheses are used in different context in python
my_set = {1, 2, 3, 4}
my_list = [1, 2, 3, 4]
my_stack = []
my_tuple = (1, 2, 3, 4) # Tuple, which is an ordered collection of items that is immutable (cannot be changed after creation).

'------------------------------------------'
# Add 2 numbers
""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list . You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] """
# Solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2): # 
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
 
"""

"""