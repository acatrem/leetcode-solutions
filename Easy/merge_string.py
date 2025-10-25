# Problem: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Time Complexity: O(n + m) where n and m are the lengths of word1 and word2
# Space Complexity: O(n + m)

class Solution:
    def mergeAlternately(self,word1: str, word2: str) -> str:
        result = []
        maxLen = max(len(word1), len(word2))

        for i in range(maxLen):
            if i < len(word1):
                result+= word1[i]
            if i < len(word2):
                result+= word2[i]

        
        return "".join(result)

        

word1 = "abc"
word2 = "pqrstu"
solution = Solution()
print(solution.mergeAlternately(word1, word2))