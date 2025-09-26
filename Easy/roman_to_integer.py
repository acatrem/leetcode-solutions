# Problem : https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1)

romanDict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

roman = "MCMXCIV"


def romanToInteger(string: str):
    result = 0
    for i in range(len(string)-1 , -1, -1):
        current = romanDict[string[i]]

        if i > 0 and current < romanDict[string[i-1]]:
            result -= current
            
        else:
            result += current
        
    return result
print(romanToInteger(roman))


