# Problem: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy
# Time Complexity: O(n) where n is the number of kids
# Space Complexity: O(n) for the result list

def kidsWithCandies(candiesList: list[int], extraCandies: int) -> list[bool]:
    boolList=[]
    for i in candiesList:
        current = i + extraCandies
        for x in range(len(candiesList)):
            if(current < candiesList[x]):
                boolList.append(False)
                break
        else:
            boolList.append(True)
    return boolList

candies=[2,3,5,1,3]
extraCandies= 3

print(kidsWithCandies(candies, extraCandies))
        


