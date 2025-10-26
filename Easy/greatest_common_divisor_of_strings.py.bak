# Problem: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Difficulty: Easy
# Time Complexity: O(n + m) where n and m are the lengths of str1 and str2
# Space Complexity: O(1)

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1.upper()
        str2.upper()

        if(str1 + str2 != str2 + str1):
            return ""
        
        gcdLength = math.gcd(len(str1), len(str2))
        return str1[:gcdLength]


