# Roman to Integer (Easy)
#
# Problem:
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol   Value: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Given a roman numeral, convert it to an integer.
# (Subtraction used when smaller numeral before larger: IV=4, IX=9, etc.)

# solution:
class Solution(object): 
  def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50,
                 'C':100, 'D':500, 'M':1000}
        total = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        total += roman[s[-1]]
        return total

# What I learned: dictionary, iterate through string, condition check for subtraction rule.
