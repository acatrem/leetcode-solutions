# Problem: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy
# Time Complexity: O(S) where S is the sum of all characters in all strings
# Space Complexity: O(1)

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if(i == len(word) or word[i] != base[i]):
                return base[0:i]
    return base
    
print(longestCommonPrefix(strs))

    