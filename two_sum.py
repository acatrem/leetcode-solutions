# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSums(numbers,target):
    numList = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                numList.append(i)
                numList.append(j)
                return numList
    
print(twoSums([2,7,11,15],9))