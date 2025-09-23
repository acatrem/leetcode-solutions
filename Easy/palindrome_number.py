# Problem: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Time Complexity: O(log10(n))
# Space Complexity: O(1)

def palindrome(number):
    
    if number < 0:
        return False
    
    digits = []
    while(number > 0):
        digits.insert(0, number % 10)
        number //= 10

    for i in range(len(digits) // 2):
        if digits[i] != digits[len(digits) -1 -i]:
            return False
    return True

print(palindrome(121))
print(palindrome(-121))
print(palindrome(10))
