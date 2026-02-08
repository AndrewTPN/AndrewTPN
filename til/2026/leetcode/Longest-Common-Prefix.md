# Longest Common Prefix (Easy)
#
# Problem:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1: Input: strs = ["flower","flow","flight"] -> Output: "fl"
# Example 2: Input: strs = ["dog","racecar","car"]     -> Output: ""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """Function that takes a list of strings as input and finds the longest common prefix."""
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            while s[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]
                
        return prefix

# What I learned: string slicing, loops, and comparing prefixes. Common in real-life when finding commonalities in data.
